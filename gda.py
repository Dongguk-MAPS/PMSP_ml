import copy
import math
import random
from typing import List
from itertools import combinations, tee
import pandas as pd
import numpy as np

MIN_DIST_BPS = False
RANGE_TOLERANCE = 1.0
POINT_STRIDE = 5

def check_distance(bps: List[float], bound_dist: float) -> bool:
    result = True
    for pair in list(pairwise(bps)):
        if abs(pair[0] - pair[1]) < bound_dist:
            result = False
    return result

def getSampleSize(ratio: float, set_size: int) -> int:
    if set_size < 1:
        raise Exception("Not Enough Sample Size")
    return max(int(ratio * set_size), 1)

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

class Gene:
    def __init__(self, feature_name: str, df_id:int, max_disc: int = 3, uniq_vals = List[float]):
        self.feature = feature_name
        if self.feature == 'Regret':
            self.disc_num = random.randint(2, max_disc)
        else:
            self.disc_num = random.randint(1, max_disc)  # 1 means out feature
        self.id = df_id
        if len(uniq_vals) == 1:
            self.disc_num = 1
        if self.disc_num > 1:
            if len(uniq_vals) < self.disc_num:
                raise ValueError('Insufficient Unique Values for Discretization - Check Dataset')
            comb_set = self.get_BPs_Comb(bps=uniq_vals, numSplits=self.disc_num)
            self.break_pts = comb_set[0]
            self.bin = None
            self.label = None
            if self.feature == 'Regret':
                pts = []
                prev_pt = 0
                for bkp in range(len(self.break_pts)+1):
                    this_pt = random.randint(prev_pt + 1, random.randint(prev_pt+2, prev_pt + 1 + POINT_STRIDE))
                    pts.append(this_pt)
                    prev_pt = this_pt
                self.point = pts

    def __repr__(self):
        name = ''
        if self.disc_num == 1:
            name = 'Feature ({0}) {1} is not selected'.format(self.id, self.feature)
        else:
            name = 'Feature ({0}) {1} discretized with {2} classes - break points: {3}'.format(self.id, self.feature, self.disc_num, self.break_pts)
        return name

    def get_BPs_Comb(self, bps: List[float], numSplits: int) -> List[tuple]:
        bounds = []
        size = len(bps)
        if size < (numSplits - 1):
            return None
        elif size == (numSplits - 1):
            return None
        else:
            bps.sort()
            for i in range(0, size - 1):
                bounds.append(((bps[i] + bps[i + 1]) / 2))

        if MIN_DIST_BPS == True:
            bound_dist = RANGE_TOLERANCE * (max(bounds) - min(bounds)) / numSplits
            comb_set = [x for x in combinations(bounds, numSplits - 1) if check_distance(x, bound_dist)]
            if len(comb_set) == 0:
                return None
            else:
                comb_set = random.choices(comb_set, k=1)

        else:
            comb_set = list(combinations(bounds, numSplits - 1))
            if len(comb_set) == 0:
                return None
            else:
                comb_set = random.choices(comb_set, k=1)
        return comb_set


class Chromosome:
    def __init__(self, attr_names: List[str], df: pd.DataFrame, cat_names: List[str]):
        gene_list = []
        for id, attr in enumerate(attr_names):
            if attr not in cat_names:
                this_bps = np.unique(df.iloc[:, id]).tolist()
                gene_list.append(Gene(feature_name=attr, max_disc=4, df_id=id, uniq_vals=this_bps))
        self.genes = gene_list
        self.objective = -1
        self.df = df

    def __repr__(self):
        return 'Chromosome with {0} features - Objective {1}'.format(len(self.genes), self.objective)

    def mutate(self):
        target_id = random.choice(range(0, len(self.genes)))
        target_gene = self.genes[target_id]
        if target_gene.disc_num == 1:
            this_bps = np.unique(self.df.iloc[:, target_gene.id]).tolist()
            self.genes[target_id] = Gene(feature_name=target_gene.feature, max_disc=4, df_id=target_gene.id, uniq_vals=this_bps)
        else:
            this_bps = np.unique(self.df.iloc[:, target_gene.id]).tolist()
            self.genes[target_id] = Gene(feature_name=target_gene.feature, max_disc=4, df_id=target_gene.id, uniq_vals=this_bps)

    def crossover(self, other: List[Gene], update_ratio=0.3):
        num_update = math.ceil(len(self.genes)*update_ratio)
        update_gene_ids = random.sample(range(0, len(self.genes)), num_update)

        for id in update_gene_ids:
            old_gene = self.genes[id]
            new_gene = next(x for x in other if x.id == old_gene.id)
            self.genes[id] = copy.deepcopy(new_gene)
        print('done')