"""
@file feasible.py
@brief Functions for feasible sub set.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE.optional_intervals_event_set import OIES


def remove_unfeasible_elements_of_Intvl_2tuple_TS(p_2tuple_TS: _2TupleTS,
                                               p_wildcard_unfeasible_2tuple_TS: _2TupleTS) -> _2TupleTS:
    """
    Remove the unfeasible elements from an instance of 2TupleTS instance.

    Args:
        (p_2tuple_TS): An instance of 2TupleTS instance
        (p_wildcard_unfeasible_2tuple_TS): An wildcard unfeasible 2TupleTS instance as pattern set.

    Returns:
        (_2TupleTS): feasible 2TupleTS instance.
    """

    feasible_Intvl_2tuple_TS: _2TupleTS = _2TupleTS()
    for _2tuple_T in p_2tuple_TS:
        # 1.1 Skip invalid _2tuple_T in wildcard_unfeasible_2tuple_TS
        if _2tuple_T in p_wildcard_unfeasible_2tuple_TS:
            continue

        # 1.2 如果通配匹配在wildcard_unfeasible_2tuple_TS, 则_2tuple_T非法, continue
        wildcard_matched: bool = False
        for op_ordered_unfeasible_Intvl_2tuple_T in p_wildcard_unfeasible_2tuple_TS:
            if _2tuple_T.is_wildcard_included(op_ordered_unfeasible_Intvl_2tuple_T):
                wildcard_matched = True
                break
        if wildcard_matched:
            continue

        # 1.3 合法, 加入到feasible_Intvl_2tuple_TS
        feasible_Intvl_2tuple_TS.add(_2tuple_T)

    # 2 ---------- result ----------

    return feasible_Intvl_2tuple_TS


def f_feasible_Intvl_2tuple_TS(p_OIE_S: OIES, p_idx_T: tuple[int,...]) -> _2TupleTS:
    """
    (definition 16) Get the feasible subset of the Cartesian product of all members of the Intvl2TupleSS instance of a finite OIES instance in an index order
    Args:
        p_OIE_S (OIES): A finite OIES instance
        p_idx_T (tuple[int,...]): An index order

    Returns:
        (_2TupleTS): The feasible subset
    """

    custom_ordered_wildcard_unfeasible_2tuple_TS: _2TupleTS = \
        p_OIE_S.get_custom_ordered_wildcard_unfeasible_Intvl_2tuple_TS(p_idx_T)

    custom_ordered_CP_of_Intvl_2tuple_SS: _2TupleTS = \
        p_OIE_S.get_custom_ordered_CP_of_Intvl_2tuple_SS(p_OIE_S.f_Intvl_2tuple_SS(), p_idx_T)

    feasible_Intvl_2tuple_TS: _2TupleTS = \
        remove_unfeasible_elements_of_Intvl_2tuple_TS(p_2tuple_TS=custom_ordered_CP_of_Intvl_2tuple_SS,
                                                   p_wildcard_unfeasible_2tuple_TS=custom_ordered_wildcard_unfeasible_2tuple_TS)

    return feasible_Intvl_2tuple_TS