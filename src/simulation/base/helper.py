"""
@file abstract_OIE.py
@brief: AbstractOIE class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/12
"""

from typing import Tuple, List
from simulation.base.structure import TwoTupleTS, TwoTupleS


def get_bound_2tupleS(p_2tupleTS: TwoTupleTS) -> TwoTupleS | None:
    """
    Get the bound 2-tuple from 2-tuple linguistic term set
    Args:
        p_2tupleTS (TwoTupleTS): source 2-tuple linguistic term set
    Returns:
        (TwoTupleS) bound 2-tuple. Return None if input is None
    """
    if p_2tupleTS is None:
        return None
    bound_2tupleS_list: List[Tuple[any, any]] = []
    bound_2tuple_map: set = set()
    for cur_2tupleT in p_2tupleTS.list():
        bound_2tuple: Tuple[float, float] = get_bound_2tuple(cur_2tupleT)
        if bound_2tuple not in bound_2tuple_map:
            bound_2tupleS_list.append(bound_2tuple)
            bound_2tuple_map.add(bound_2tuple)
    return TwoTupleS(*bound_2tupleS_list)


def get_bound_2tuple(p_2tupleT: Tuple[Tuple[float, float]]) -> Tuple[float, float] | None:
    """
    (definition 19)Get the bound 2-tuple of a tuple of 2-tuples with a limited length.
    Args:
        p_2tupleT (Tuple[Tuple[float, float]]): A _2TupleT instance with a limited length
    Returns:
        (Tuple[float, float]): Bound 2-tuple
    """
    if p_2tupleT is None or len(p_2tupleT) == 0:
        return None
    min_1st: float = p_2tupleT[0][0]
    max_2nd: float = p_2tupleT[0][1]
    for cur_2tuple in p_2tupleT:
        if min_1st > cur_2tuple[0]:
            min_1st = cur_2tuple[0]
        if max_2nd < cur_2tuple[1]:
            max_2nd = cur_2tuple[1]

    return min_1st, max_2nd


def is_wildcard_matched(p_2tupleT: Tuple[Tuple | str, ...],
                        p_pattern_2tupleT: Tuple[Tuple | str, ...]
                        ) -> bool:
    """
    Check if there is wildcard inclusion.
    Args:
        p_2tupleT:
        p_pattern_2tupleT (_2TupleT): pattern, use '*' for wildcard
    Returns:
        (bool): result
    """
    if len(p_2tupleT) != len(p_pattern_2tupleT):
        return False
    for i in range(0, len(p_2tupleT)):
        if p_pattern_2tupleT[i] != p_2tupleT[i] and p_pattern_2tupleT[i] != '*':
            return False
    return True


def f_min_1_of_2tupleT(p_2tupleT: Tuple[Tuple,...]) -> object:
    """
    (definition 17/function 1)Obtain the minimum 1st item of a 2TupleT instance
    Args:
        p_2tupleT (_2TupleT): An _2TupleT instance
    Returns:
        (object): the minimum 1st item
    """
    if p_2tupleT is None:
        return None
    min_1st: object = p_2tupleT[0][0]
    for cur_2tuple in p_2tupleT:
        if min_1st > cur_2tuple[0]:
            min_1st = cur_2tuple[0]
    return min_1st


def f_max_2_of_2tupleT(p_2tupleT: Tuple[Tuple,...]) -> object:
    """
    (definition 17/function 2)Obtain the maximum 2nd item of a 2TupleT instance
    Args:
        p_2tupleT (_2TupleT): An _2TupleT instance
    Returns:
        (object): the maximum 2nd item
    """
    if p_2tupleT is None:
        return None
    max_2nd: object = p_2tupleT[0][1]
    for _2tuple in p_2tupleT:
        if max_2nd < _2tuple[1]:
            max_2nd = _2tuple[1]
    return max_2nd
