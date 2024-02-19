from module import *
import copy
import pandas as pd
from chefboost import Chefboost as chef
import retrieval
from gda import *
import priority_functions

JS_Model = None
MA_Model = None

MAX_DEPTH = 5


def discrete_df(df: pd.DataFrame, chromo: Chromosome):
    # final_columns = [gene.feature for gene in chromo.genes if gene.disc_num != 1]
    # df = df.drop(columns=[col for col in df if col not in final_columns])
    for gene in chromo.genes:
        if gene.disc_num == 1:
            df = df.drop(columns=[gene.feature])
            continue
        if gene.feature != 'Regret':
            bin = [float('-inf')]
            label = []
            for i in range(len(gene.break_pts)):
                bin.append(gene.break_pts[i])
                label.append('Less_{0}'.format(gene.break_pts[i]))
            bin.append(float('inf'))
            label.append('Greater_{0}'.format(gene.break_pts[i]))
            gene.bin = bin
            gene.label = label
            df[gene.feature] = pd.cut(df[gene.feature], bins=bin, labels=label)
            df[gene.feature] = df[gene.feature].astype('object')
        else:
            bin = [float('-inf')]
            label = []
            # No difference in regret - zero point
            bin.append(0)
            label.append('{0}'.format(0))
            prev_pt = 0
            for i in range(len(gene.break_pts)):
                bin.append(gene.break_pts[i])
                # pt = (prev_pt+gene.break_pts[i])/2
                label.append('{0}'.format(gene.point[i]))
                # label.append('{0}'.format(i+1))
                # prev_pt = gene.break_pts[i]
            bin.append(float('inf'))
            label.append('{0}'.format(gene.point[i+1]))
            # label.append('{0}'.format(i+2))
            gene.bin = bin
            gene.label = label
            df[gene.feature] = pd.cut(df[gene.feature], bins=bin, labels=label)
            df[gene.feature] = df[gene.feature].astype('object')
    return df


def get_regret(row: List, model) -> float:
    return chef.predict(model, row)


def learn_model(js_path: str = 'datasets/js.csv', ma_path: str = 'datasets/ma.csv', discretize: bool = False, chromo: List[Chromosome] = None):
    if discretize is False:
        df_js = pd.read_csv(js_path, encoding_errors='ignore')
        df_ma = pd.read_csv(ma_path, encoding_errors='ignore')
        df_js = df_js.drop(columns=retrieval.DROP_FEATURES_JS_JM)
        df_ma = df_ma.drop(columns=retrieval.DROP_FEATURES_MA_JM)
        config = {'algorithm': 'Regression', 'max_depth': MAX_DEPTH, 'enableParallelism': False}
        model_js = chef.fit(df_js, config, target_label='Regret')
        model_ma = chef.fit(df_ma, config, target_label='Regret')
    else:
        df_js = pd.read_csv(js_path, encoding_errors='ignore')
        df_ma = pd.read_csv(ma_path, encoding_errors='ignore')
        df_js = df_js.drop(columns=retrieval.DROP_FEATURES_JS_JM)
        df_ma = df_ma.drop(columns=retrieval.DROP_FEATURES_MA_JM)

        df_js = discrete_df(df_js, chromo[0])
        df_ma = discrete_df(df_ma, chromo[1])

        config = {'algorithm': 'C4.5', 'max_depth': MAX_DEPTH, 'enableParallelism': False}
        model_js = chef.fit(df_js, config, target_label='Regret', name='js_disc')
        model_ma = chef.fit(df_ma, config, target_label='Regret', name='ma_disc')

    return model_js, model_ma


def learn_model_sep(js_path: str = 'datasets/js.csv', ma_path: str = 'datasets/ma.csv'):
    df_js = pd.read_csv(js_path, encoding_errors='ignore')
    df_ma = pd.read_csv(ma_path, encoding_errors='ignore')
    df_js = df_js.drop(columns=retrieval.DROP_FEATURES_JS_JM)
    df_ma = df_ma.drop(columns=retrieval.DROP_FEATURES_MA_JM)

    df_js_binary = df_js.copy()
    df_js_binary.loc[df_js_binary['Regret'] != 0, 'Regret'] = 'Yes'
    df_js_binary.loc[df_js_binary['Regret'] == 0, 'Regret'] = 'No'

    df_ma_binary = df_ma.copy()
    df_ma_binary.loc[df_ma_binary['Regret'] != 0, 'Regret'] = 'Yes'
    df_ma_binary.loc[df_ma_binary['Regret'] == 0, 'Regret'] = 'No'

    config = {'algorithm': 'C4.5', 'max_depth': MAX_DEPTH, 'enableParallelism': False}
    model_js_binary = chef.fit(df_js_binary, config, target_label='Regret', name='js_binary')
    model_ma_binary = chef.fit(df_ma_binary, config, target_label='Regret', name='ma_binary')

    df_js = df_js[df_js['Regret'] > 0]
    df_ma = df_ma[df_ma['Regret'] > 0]

    config = {'algorithm': 'Regression', 'max_depth': MAX_DEPTH, 'enableParallelism': False}
    model_js = chef.fit(df_js, config, target_label='Regret', name='js')
    model_ma = chef.fit(df_ma, config, target_label='Regret', name='ma')

    return model_js_binary, model_js, model_ma_binary, model_ma


def ml_scheduling(_prob: Instance, model_js, model_ma, ml_alg: str = 'None', discretize: bool = False, chromo: List[Chromosome] = None):
    prob = copy.deepcopy(_prob)

    def prioritize_jobs(job_list: List[Job]):
        if ml_alg == 'DT':
            for JobA in job_list:
                for JobB in job_list:
                    if JobA is not JobB:
                        func = retrieval.update_features()
                        row = retrieval.add_row_js(pd.DataFrame(), prob, JobA, JobB, 0, no_label=True, func=func)
                        row = discrete_df(row, chromo[0])
                        regret = get_regret(model=model_js, row=row.values.tolist()[0])
                        JobA.priority += float(regret)

        else:  # If there is no rule, randomly select
            for job in job_list:
                job.priority = random.uniform(0.0, 1.0)
        return sorted((job for job in job_list if job.complete is False), key=lambda j: j.priority)

    def prioritize_mchs(mch_list: List[Machine], chosen_job: Job):
        if ml_alg == 'DT':
            for MchA in mch_list:
                for MchB in mch_list:
                    if MchA is not MchB:
                        row = retrieval.add_row_ma(pd.DataFrame(), prob, MchA, MchB, 0, chosen_job, no_label=True)
                        row = discrete_df(row, chromo[1])
                        regret = get_regret(model=model_ma, row=row.values.tolist()[0])
                        MchA.priority += float(regret)

        else:  # If there is no rule, randomly select
            for mch in mch_list:
                mch.priority = random.uniform(0.0, 1.0)
        return sorted((mch for mch in mch_list), key=lambda m: m.priority)

    wait_jobs = prioritize_jobs(prob.job_list)

    while len(wait_jobs) != 0:
        chosen_job = wait_jobs[0]
        sorted_mchs = prioritize_mchs(prob.machine_list, chosen_job)
        chosen_mch = sorted_mchs[0]
        chosen_mch.process(chosen_job)
        wait_jobs = prioritize_jobs(prob.job_list)

    obj = get_obj(prob)
    result = Schedule('ML Scheduling with {0}'.format(ml_alg), prob, obj=obj)
    # result.print_schedule()

    return result


def ml_scheduling_sep(_prob: Instance, model_js_binary, model_js, model_ma_binary, model_ma, ml_alg: str = 'None'):
    prob = copy.deepcopy(_prob)

    def prioritize_jobs(job_list: List[Job]):
        if ml_alg == 'DT':
            for JobA in job_list:
                for JobB in job_list:
                    if JobA is not JobB:
                        row = retrieval.add_row_js(pd.DataFrame(), prob, JobA, JobB, 0, no_label=True)
                        diff = get_regret(model=model_js_binary, row=row)
                        if diff == 'Yes':
                            regret = get_regret(model=model_js, row=row)
                            JobA.priority += regret
                            # JobA.priority += 1
                        else:
                            continue

        else:  # If there is no rule, randomly select
            for job in job_list:
                job.priority = random.uniform(0.0, 1.0)
        return sorted((job for job in job_list if job.complete is False), key=lambda j: j.priority)

    def prioritize_mchs(mch_list: List[Machine], chosen_job: Job):
        if ml_alg == 'DT':
            for MchA in mch_list:
                for MchB in mch_list:
                    if MchA is not MchB:
                        row = retrieval.add_row_ma(pd.DataFrame(), prob, MchA, MchB, 0, chosen_job, no_label=True)
                        diff = get_regret(model=model_ma_binary, row=row)
                        if diff == 'Yes':
                            regret = get_regret(model=model_ma, row=row)
                            MchA.priority += regret
                            # MchA.priority += 1
                        else:
                            continue

        else:  # If there is no rule, randomly select
            for mch in mch_list:
                mch.priority = random.uniform(0.0, 1.0)
        return sorted((mch for mch in mch_list), key=lambda m: m.priority)

    wait_jobs = prioritize_jobs(prob.job_list)

    while len(wait_jobs) != 0:
        chosen_job = wait_jobs[0]
        sorted_mchs = prioritize_mchs(prob.machine_list, chosen_job)
        chosen_mch = sorted_mchs[0]
        chosen_mch.process(chosen_job)
        wait_jobs = prioritize_jobs(prob.job_list)

    obj = get_obj(prob)
    result = Schedule('ML Scheduling with {0}'.format(ml_alg), prob, obj=obj)
    # result.print_schedule()

    return result