from module import *
import copy


def scheduling(_prob: Instance, rule: str) -> Schedule:
    '''
    This function is for finding a feasible solution for a given scheduling problem instance.
    :param prob: Problem Instance
    :param rule: Scheduling Rule (e.g. EDD, SPT, MST)
    :return: Schedule Result with Objective Function
    '''

    prob = copy.deepcopy(_prob)

    def normalize_weights(n:int):
        list_weights= []
        for i in range(n):
            list_weights.append(random.uniform(0, 10))
        total = sum(list_weights)  # 가중치의 합 계산
        normalized_weights = [weight / total for weight in list_weights]
        return normalized_weights

    def update_priority(job_list, mch_list):
        for j in job_list:
            if j.complete is False:
                if rule == 'EDD':
                    j.priority = j.due
                elif rule == 'SPT':  # This is an example of SPT
                    # j.priority = sum([m.ptime[j.ID] for m in mch_list])
                    j.priority = min(mch_list, key=lambda m: m.available).ptime[j.ID]
                elif rule == 'MST':  # This is an example of MST (Minimum Setup Time)
                    j.priority = min(mch_list, key=lambda m: m.available).get_setup(j)
                elif rule == 'LPT':
                    j.priority = -min(mch_list, key=lambda m: m.available).ptime[j.ID]
                elif rule == 'SECT':
                    if min(mch_list, key=lambda m: m.available) == 0 :
                        j.priority = min(mch_list, key=lambda m: m.available).ptime[j.ID]
                    else:
                        j.priority = min(mch_list, key=lambda m: m.available).ptime[j.ID] + min(mch_list, key=lambda m: m.available).get_setup(j)
                elif rule == 'mix':
                    weight = normalize_weights(len(job_list))
                    sum_value = 0

                    spt = min(mch_list, key=lambda m: m.available).ptime[j.ID]
                    mst = min(mch_list, key=lambda m: m.available).get_setup(j)
                    lpt = -min(mch_list, key=lambda m: m.available).ptime[j.ID]
                    if min(mch_list, key=lambda m: m.available) == 0:
                        sect = min(mch_list, key=lambda m: m.available).ptime[j.ID]
                    else:
                        sect = min(mch_list, key=lambda m: m.available).ptime[j.ID] + \
                                     min(mch_list, key=lambda m: m.available).get_setup[j]
                    method_value=[spt,mst,lpt,sect]
                    for n in range(len(weight)):
                        sum_value += weight[n] * method_value[n]
                    j.priority = sum_value

                else: # If there is no rule, randomly select
                    j.priority = random.uniform(0.0, 1.0)
        return sorted((job for job in job_list if job.complete is False), key=lambda j: j.priority)

    wait_jobs = update_priority(prob.job_list, prob.machine_list)

    while len(wait_jobs) != 0:
        machines = sorted((mch for mch in prob.machine_list), key=lambda m: m.available)
        machines[0].process(wait_jobs[0])
        wait_jobs = update_priority(prob.job_list, prob.machine_list)

    obj = get_obj(prob)
    result = Schedule(rule, prob, obj=obj)
    result.print_schedule()

    return result
