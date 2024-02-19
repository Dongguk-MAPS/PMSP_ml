from heuristic import scheduling
import random
import math



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

