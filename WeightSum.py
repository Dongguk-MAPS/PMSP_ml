from heuristic import scheduling
from module import generate_prob
import random
import math
import numpy as np


def generate_random_weights():  # initial 가중치 생성
    weights = [random.random() for _ in range(4)]
    total = sum(weights)
    normalized_weights = [w / total for w in weights]
    return normalized_weights


def change_weights(current_weights, change_factor=1):
    new_weights = [w * (1 + random.uniform(0, change_factor)) for w in current_weights]
    total = sum(new_weights)
    normalized_weights = [w / total for w in new_weights]
    return normalized_weights


def find_average(nums):
    total = sum(nums)
    return total / len(nums) if len(nums) > 0 else 0


def local_search(test_instance_lst, iterations=100, change_factor=0.1, temperature=1.0):
    current_weights = generate_random_weights()
    current_score = 0

    for test_instance in test_instance_lst:
        current_score += scheduling(test_instance, 'MIX', current_weights).objective

    for i in range(1, iterations + 1):
        temp = temperature * math.exp(-0.01 * i)
        new_weights = change_weights(current_weights, change_factor)
        new_score = 0

        for test_instance in test_instance_lst:
            new_score += scheduling(test_instance, 'MIX', new_weights).objective

        if new_score < current_score or random.random() < math.exp(-(new_score - current_score) / temp):
            current_weights = new_weights
            current_score = new_score

    return current_weights, current_score / 10


results = {}
mix_list = []
weights_list = []
test_instance_lst = []

for index in range(1, 11):
    test_instance = generate_prob(numJob=8, numMch=3, tau=0.2)
    test_instance.loadFile(f'datasets/train_small/pmsp_sdst_{index}.prob')
    test_instance_lst.append(test_instance)

score_lst = []
for i in range(10):
    optimal_weights, optimal_score = local_search(test_instance_lst=test_instance_lst, iterations=1000,
                                               change_factor=0.1, temperature=1.0)
    score_lst.append(optimal_score)

print(find_average(score_lst))

# # 각 문제에 대해 30번의 반복 실행
    # for i in range(30):
    #     optimal_weights, optimal_score = local_search(test_instance_lst=test_instance_lst, iterations=1000, change_factor= 0.1, temperature=1.0)
    #     # schedule_mix= scheduling(test_instance, 'MIX', optimal_weights)

        # mix_list.append(optimal_score)
        # weights_list.append(optimal_weights)

    # # 각 prob에 대한 평균 최적값 계산
    # avg_optimal_score = find_average(mix_list)
    #
    # # 가중치의 평균 계산
    # avg_weights = np.mean(weights_list, axis=0)
    #
    # # 평균 가중치를 이용하여 최적값 계산
    # optimal_score_with_avg_weights = scheduling(test_instance, 'MIX', avg_weights).objective

    # 결과를 txt 파일에 저장
    # with open(f'pmsp_sdst_{index}_result.txt', 'w') as f:
    #     f.write(f'Average optimal score for pmsp_sdst_{index}: {avg_optimal_score}\n')
    #     f.write(f'Average weights for pmsp_sdst_{index}: {avg_weights}\n')
    #     f.write(f'Optimal score with average weights for pmsp_sdst_{index}: {optimal_score_with_avg_weights}\n')

#     # 결과를 결과 딕셔너리에 저장
#     results[f'pmsp_sdst_{index}'] = {
#         'avg_optimal_score': avg_optimal_score,
#         'avg_weights': avg_weights,
#         'optimal_score_with_avg_weights': optimal_score_with_avg_weights
#     }
#


# weight= [0.20583963, 0.26134453, 0.32452051, 0.20829533]
# for i in range(1,31):
#     test_instance = generate_prob(numJob=8, numMch=3, tau=0.2)
#     test_instance.loadFile(f'datasets/train/pmsp_sdst_{i}.prob')
#     schedule_mix = scheduling(test_instance, 'MIX', weight)
#     print(i," 번째 ", schedule_mix.objective)