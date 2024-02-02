import random
from typing import List
from itertools import combinations, tee
import pandas as pd
import numpy as np

MIN_DIST_BPS = False
RANGE_TOLERANCE = 1.0

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
        self.disc_num = random.randint(2, max_disc)
        self.id = df_id
        if len(uniq_vals) < self.disc_num:
            raise ValueError('Insufficient Unique Values for Discretization - Check Dataset')
        comb_set = self.get_BPs_Comb(bps=uniq_vals, numSplits=self.disc_num)
        self.break_pts = comb_set[0]
        self.bin = None
        self.label = None

    def __repr__(self):
        return 'Feature ({0}) {1} discretized with {2} classes - break points: {3})'.format(self.id, self.feature, self.disc_num, self.break_pts)

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