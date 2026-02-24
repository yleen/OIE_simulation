

import random
from simulation.base.structure import TwoTupleS, TwoTupleTS


def get_rand_2tuple(p_2tupleS: TwoTupleS):
    return p_2tupleS[random.randrange(0, len(p_2tupleS), 1)]

def get_rand_2tupleT(p_2tupleTS: TwoTupleTS):
    return p_2tupleTS[random.randrange(0, len(p_2tupleTS), 1)]
