"""
@file feasible.py
@brief Functions for feasible sub set.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""
from simulation.base.helper import is_wildcard_matched
from simulation.base.structure import TwoTupleTS, TwoTupleSS
from simulation.oie.optional_intervals_event_set import OIES


def remove_infeasible_elements_of_interval_2tupleTS(p_2tupleTS: TwoTupleTS,
                                                    p_wildcard_infeasible_2tupleTS: TwoTupleTS) -> TwoTupleTS:
    """
    Remove the unfeasible elements from an instance of 2TupleTS instance.
    Args:
        p_2tupleTS (TwoTupleTS): An instance of 2TupleTS instance
        p_wildcard_infeasible_2tupleTS (TwoTupleTS): An wildcard infeasible 2TupleTS instance as pattern set.
    Returns:
        (TwoTupleTS): feasible 2TupleTS instance.
    """

    feasible_2tupleTS: TwoTupleTS = TwoTupleTS()
    for cur_2tupleT in p_2tupleTS:
        # 1.1 Skip invalid cur_2tupleT in wildcard_unfeasible_2tuple_TS
        if cur_2tupleT in p_wildcard_infeasible_2tupleTS:
            continue

        # 1.2 如果通配匹配在wildcard_unfeasible_2tuple_TS, 则_2tuple_T非法, continue
        wildcard_matched: bool = False
        for infeasible_2tupleT in p_wildcard_infeasible_2tupleTS:
            if is_wildcard_matched(cur_2tupleT, infeasible_2tupleT):
                wildcard_matched = True
                break
        if wildcard_matched:
            continue

        # 1.3 合法, 加入到feasible_2tupleTS
        feasible_2tupleTS.add(cur_2tupleT)

    # 2 ---------- result ----------

    return feasible_2tupleTS


def get_feasible_2tupleTS(p_oieS: OIES, p_idxT: tuple[int,...]) -> TwoTupleTS:
    """
    (definition 16) Get the feasible subset of the Cartesian product of all members of the Intvl2TupleSS instance of a finite OIES instance in an index order
    Args:
        p_oieS (OIES): A finite OIES instance
        p_idxT (tuple[int,...]): An index order
    Returns:
        (TwoTupleTS): The feasible subset
    """
    wildcard_infeasible_2tupleTS: TwoTupleTS = \
        p_oieS.get_infeasible_2tupleTS(p_idxT)

    interval_2tupleSS: TwoTupleSS = p_oieS.get_interval_2tupleSS()
    cp_of_2tupleSS: TwoTupleTS = p_oieS.get_CP_of_Interval_2tupleSS(interval_2tupleSS, p_idxT)

    feasible_2tupleTS: TwoTupleTS = \
        remove_infeasible_elements_of_interval_2tupleTS(p_2tupleTS=cp_of_2tupleSS,
                                                        p_wildcard_infeasible_2tupleTS=wildcard_infeasible_2tupleTS)
    return feasible_2tupleTS