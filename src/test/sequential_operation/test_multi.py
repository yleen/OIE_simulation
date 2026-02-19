"""
@file test_multi.py
@brief Test cases of complete sequential multiplication.
@author li.zhong.yuan@outlook.com
@date 2025/1/28
"""
from simulation.base.structure import TwoTupleTS
from simulation.oie.optional_intervals_event_set import OIES
from simulation.sequential_operation.multiplication.complete_sequential_multiplication import \
    complete_sequential_multiplication
from test.instance import atomOie_1, atomOie_2


def test_multiplication_valid_1():
    oieS: OIES = OIES(atomOie_1, atomOie_2)
    infeasible_2tupleTS: TwoTupleTS = TwoTupleTS()
    oieS.set_wildcard_infeasible_2tupleTS(p_wildcard_infeasible_2tupleTS=infeasible_2tupleTS,
                                          p_oieT=(atomOie_1, atomOie_2))
    oie_res = complete_sequential_multiplication(p_oieS=oieS, p_idxT=(1, 2))
    print(f"oie_res: {str(oie_res)}\n")

