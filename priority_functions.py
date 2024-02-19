import math

from module import *

MULTIVALUE_CRITERIA = 'Avg'

def slack(prob: Instance, job: Job):
    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    earliest_available = min(prob.machine_list, key=lambda x: x.available).available
    slack = job.due - earliest_available - (ptimes[MULTIVALUE_CRITERIA]+setups[MULTIVALUE_CRITERIA])
    return slack

def mdd(prob: Instance, job: Job):
    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    earliest_available = min(prob.machine_list, key=lambda x: x.available).available
    slack = job.due - earliest_available - (ptimes[MULTIVALUE_CRITERIA]+setups[MULTIVALUE_CRITERIA])
    mdd = 0
    if slack > 0:
        mdd = job.due
    else:
        mdd = earliest_available + (ptimes[MULTIVALUE_CRITERIA]+setups[MULTIVALUE_CRITERIA])
    return mdd

def rt(prob: Instance, job: Job):
    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    rt = job.due - (ptimes[MULTIVALUE_CRITERIA]+setups[MULTIVALUE_CRITERIA])
    return rt

def cr(prob: Instance, job: Job):
    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    earliest_available = min(prob.machine_list, key=lambda x: x.available).available
    cr = (job.due - earliest_available)/(ptimes[MULTIVALUE_CRITERIA]+setups[MULTIVALUE_CRITERIA])
    return cr

def atc(prob: Instance, job: Job, k=0.1):
    avg_ptimes = 0
    waiting_jobs = 0
    for job in prob.job_list:
        if job.complete == False:
            avg_ptimes += job.get_ptimes(prob.machine_list)['Avg']
            waiting_jobs += 1
    if waiting_jobs == 0:
        return 10000
    avg_ptimes = avg_ptimes/waiting_jobs

    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    earliest_available = min(prob.machine_list, key=lambda x: x.available).available
    slack = job.due - earliest_available - (ptimes[MULTIVALUE_CRITERIA] + setups[MULTIVALUE_CRITERIA])
    atc = math.exp(-(max(0, slack)/(k*avg_ptimes)))/ptimes[MULTIVALUE_CRITERIA]
    return atc

def covert(prob: Instance, job: Job, k=0.1):
    ptimes = job.get_ptimes(prob.machine_list)
    setups = job.get_setups(prob.machine_list)
    earliest_available = min(prob.machine_list, key=lambda x: x.available).available
    slack = job.due - earliest_available - (ptimes[MULTIVALUE_CRITERIA] + setups[MULTIVALUE_CRITERIA])
    covert = max(0, 1-(max(0, slack)/(k*ptimes[MULTIVALUE_CRITERIA])))
    covert = covert/ptimes[MULTIVALUE_CRITERIA]
    return covert