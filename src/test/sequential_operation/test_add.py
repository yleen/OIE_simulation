"""
@file test_add.py
@brief Test cases of complete sequential addition.
@author li.zhong.yuan@outlook.com
@date 2025/1/27
"""
from simulation.base.structure import TwoTupleTS
from simulation.sequential_operation.addition.complete_sequential_addition import complete_sequential_addition
from simulation.oie.optional_intervals_event_set import OIES
from test.instance import atomOie_1, atomOie_2


def test_addition_with_identical_operands():
    # ---------- 1 Init an OIES instance ----------
    oieS = OIES(atomOie_1, atomOie_1)
    # ---------- 2 Set infeasible 2TupleTS instance to the OIES instance ----------
    # 2.1  Init an infeasible 2TupleTS instance, empty set
    infeasible_2tupleTS = TwoTupleTS()
    # 2.2 Assign to the member of OIES instance
    oieS.set_wildcard_infeasible_2tupleTS(infeasible_2tupleTS, (atomOie_1, atomOie_1))
    # ---------- 3 Complete Sequential Addition ----------
    domain_filtering_2tuple = (1, 5)
    oie_res = complete_sequential_addition(oieS, (1, 2), domain_filtering_2tuple)
    print(f"oie_res: {str(oie_res)}\n")


def test_addition_valid_1():
    oieS = OIES(atomOie_1, atomOie_2)

    infeasible_2tupleTS = TwoTupleTS()
    oieS.set_wildcard_infeasible_2tupleTS(infeasible_2tupleTS, (atomOie_1, atomOie_1))

    domain_filtering_2tuple = (1, 5)
    oie_res = complete_sequential_addition(oieS, (1, 2), domain_filtering_2tuple)

    print(f"oie_res: {str(oie_res)}\n")


