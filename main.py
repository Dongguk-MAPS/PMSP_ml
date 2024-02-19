from pulp import pulp, LpStatusOptimal, LpStatus
from module import *
from milp import *
from cp import *
import heuristic
import random
import time
import multiprocessing
import pickle
import pandas as pd
from gurobi import *
from pp import pulp_scheduling
import typing
from retrieval import *
from ml_heuristic import *
from statistics import mean
import csv

if __name__ == '__main__':
    record = []

    # test_instance = generate_prob(numJob=5, numMch=2, tau=0.2)
    # retrieve_decisions_rh(_prob=test_instance)
    with open('datasets/best.disc', mode='rb') as fr:
        best = pickle.load(fr)
    best_chromo = best
    for p in range(0, 100):
        new_chromo = copy.deepcopy(best)
        new_chromo[1].mutate()
        new_chromo[2].mutate()
        model_js, model_ma = learn_model(discretize=True, chromo=[new_chromo[1], new_chromo[2]])
        perf = []
        for i in range(10):
            numJob = random.randint(5, 10)
            test_instance = generate_prob(numJob=numJob, numMch=2, tau=0.2)
            test_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i + 1))
            schedule_ml = ml_scheduling(test_instance, model_js, model_ma, 'DT', True, [new_chromo[1], new_chromo[2]])
            perf.append(schedule_ml.objective)
        if sum(perf) / len(perf) < best_chromo[0]:
            best_chromo = [sum(perf) / len(perf), new_chromo[1], new_chromo[2]]
            with open('datasets/best.disc', mode='wb') as fw:
                pickle.dump(best_chromo, fw)

    # model_js, model_ma = learn_model(discretize=True, chromo=[best[1], best[2]])
    # for i in range(10):
    #     numJob = random.randint(5, 10)
    #     test_instance = generate_prob(numJob=numJob, numMch=2, tau=0.2)
    #     # test_instance.saveFile('datasets/train/pmsp_sdst_{0}.prob'.format(i + 1))
    #     test_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i + 1))
    #     # schedule_rh = retrieve_decisions_rh(test_instance)
    #     schedule_ml = ml_scheduling(test_instance, model_js, model_ma, 'DT', True, [best[1], best[2]])
    #     schedule_mst = scheduling(test_instance, 'MST')
    #     schedule_cp = cp_scheduling(test_instance, time_limit=600, init_sol=schedule_mst)
    #     record.append([schedule_ml.objective, schedule_cp.objective])


    # model_js_binary, model_js, model_ma_binary, model_ma = learn_model_sep()
    df_js = pd.read_csv('datasets/js.csv', encoding_errors='ignore')
    df_ma = pd.read_csv('datasets/ma.csv', encoding_errors='ignore')

    prior_func = update_features()
    df_js = df_js.drop(columns=retrieval.DROP_FEATURES_JS_JM)
    df_ma = df_ma.drop(columns=retrieval.DROP_FEATURES_MA_JM)
    col_js = list(df_js.columns)
    col_ma = list(df_ma.columns)

    pop = []

    for p in range(0, 20):
        chromo_js = Chromosome(col_js, df_js, cat_names=retrieval.CAT_FEATURES_JS_JM)
        chromo_ma = Chromosome(col_ma, df_ma, cat_names=retrieval.CAT_FEATURES_MA_JM)
        model_js, model_ma = learn_model(discretize=True, chromo=[chromo_js, chromo_ma])
        perf = []
        for i in range(10):
            numJob = random.randint(5, 10)
            test_instance = generate_prob(numJob=numJob, numMch=2, tau=0.2)
            test_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i + 1))
            schedule_ml = ml_scheduling(test_instance, model_js, model_ma, 'DT', True, [chromo_js, chromo_ma])
            perf.append(schedule_ml.objective)
        pop.append([sum(perf)/len(perf), chromo_js, chromo_ma])
        print(sum(perf)/len(perf))

    pop.sort(key=lambda x: x[0])
    survivor_ratio = 0.3
    survivor_id = math.ceil(len(pop)*survivor_ratio)
    best_chromo = best
    # with open('datasets/best.disc', mode='wb') as fw:
    #     pickle.dump(best_chromo, fw)

    for g in range(0, 20):
        survivors = pop[:survivor_id]
        while len(survivors) < 20:
            new_chromo = copy.deepcopy(best_chromo)
            new_chromo[1].mutate()
            new_chromo[2].mutate()
            model_js, model_ma = learn_model(discretize=True, chromo=[new_chromo[1], new_chromo[2]])
            perf = []
            for i in range(10):
                numJob = random.randint(5, 10)
                test_instance = generate_prob(numJob=numJob, numMch=2, tau=0.2)
                test_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i + 1))
                schedule_ml = ml_scheduling(test_instance, model_js, model_ma, 'DT', True, [new_chromo[1], new_chromo[2]])
                perf.append(schedule_ml.objective)
            survivors.append([sum(perf) / len(perf), new_chromo[1], new_chromo[2]])
            if sum(perf) / len(perf) < best_chromo[0]:
                best_chromo = [sum(perf) / len(perf), new_chromo[1], new_chromo[2]]
                with open('datasets/best.disc', mode='wb') as fw:
                    pickle.dump(best_chromo, fw)
        survivors.sort(key=lambda x: x[0])
        pop = survivors
    print('Evolve')


    chromo_js = Chromosome(col_js, df_js, cat_names=retrieval.CAT_FEATURES_JS_JM)
    chromo_js_2 = Chromosome(col_js, df_js, cat_names=retrieval.CAT_FEATURES_JS_JM)
    chromo_ma = Chromosome(col_ma, df_ma, cat_names=retrieval.CAT_FEATURES_MA_JM)

    for i in range(100):
        chromo_js.mutate()
        chromo_js_2.mutate()
        chromo_js.crossover(chromo_js_2.genes)

    trials = []
    for j in range(100):
        col_js = list(df_js.columns)
        col_ma = list(df_ma.columns)
        chromo_js = Chromosome(col_js, df_js, cat_names=retrieval.CAT_FEATURES_JS_JM)
        chromo_ma = Chromosome(col_ma, df_ma, cat_names=retrieval.CAT_FEATURES_MA_JM)
        model_js, model_ma = learn_model(discretize=True, chromo=[chromo_js, chromo_ma])
        record = []
        for i in range(30):
            numJob = random.randint(10, 20)
            test_instance = generate_prob(numJob=numJob, numMch=3, tau=0.2)
            # test_instance.saveFile('datasets/train/pmsp_sdst_{0}.prob'.format(i+1))
            test_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i+1))
            # schedule_ml = ml_scheduling_sep(test_instance, model_js_binary, model_js, model_ma_binary, model_ma, 'DT')
            schedule_ml = ml_scheduling(test_instance, model_js, model_ma, 'DT', chromo=[chromo_js, chromo_ma])
            record.append(schedule_ml.objective)
        trials.append((sum(record)/len(record)))


        # schedule_rh = retrieve_decisions_rh(test_instance)
        # new_instance = generate_prob(numJob=5, numMch=3, tau=0.2)
        # new_instance.loadFile('datasets/train/pmsp_sdst_{0}.prob'.format(i+1))

        # schedule = heuristic.scheduling(test_instance, 'MST')
        # schedule = milp_scheduling(test_instance)
        schedule_mst = scheduling(test_instance, 'MST')
        # schedule_cp = cp_scheduling(test_instance, time_limit=3600, init_sol=schedule_mst)
        schedule_spt = scheduling(test_instance, 'SPT')
        schedule_rnd = scheduling(test_instance, 'RND')

        # record.append([schedule_cp.objective, schedule_spt.objective, schedule_mst.objective, schedule_rnd.objective, schedule_ml.objective])
        record.append([schedule_ml.objective, schedule_mst.objective, schedule_spt.objective, schedule_rnd.objective])
        # result = schedule_cp
        # cp_initial = result.objective
        # imp_cnt = 0
        # while result is not None:
        #     temp_schedule = retrieve_decisions(test_instance, result)
        #     if temp_schedule is None:
        #         with open('datasets/train/pmsp_sdst_{0}.cp'.format(i+1), mode='wb') as fw:
        #             pickle.dump(result, fw)
        #         print('Done')
        #     else:
        #         imp_cnt += 1
        #         result = temp_schedule
        #         if imp_cnt == 3:
        #             imp_cnt = 0
        #             result = cp_scheduling(test_instance, time_limit=600, init_sol=result)
        #             print('Check - Reinitiate the warm-start process with result')

    print(*map(mean, zip(*record)))
    with open('out.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(record)
    print('EOP')

    # pd.cut(df["Yourcolumns"],
    #        bins=[0, 2.5, 3, 3.25, 3.5, 3.75, 4],
    #        labels=["Very bad", "Bad", "Average", "good", "Very good", "Excellent"])
    # this_bps = np.unique(data[:, attr.id]).tolist()

    #schedule.print_schedule()
    #draw_gantt_chart(schedule, test_instance)

    # schedule = milp_scheduling(test_instance)
    # schedule.print_schedule()
    #draw_gantt_chart(schedule, test_instance)

    # schedule = cp_scheduling(test_instance)
    # schedule = milp_scheduling_ortools(test_instance)
    # schedule = cp_scheduling_ortools(test_instance)
