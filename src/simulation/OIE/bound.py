"""
@file bound.py
@brief Functions for bound 2-tuple.
@author li.zhong.yuan@outlook.com
@date 2025/2/9
"""


from typing import List
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_S import _2TupleS
from simulation.OIE._2Tuple_TS import _2TupleTS


def get_bound_2tuple_S(p_2tupleT_S: _2TupleTS) -> _2TupleS | None:
    """
    Get the bound 2-tuple from 2-tuple linguistic term set
    Args:
        p_2tupleT_S (_2TupleTS): source 2-tuple linguistic term set

    Returns:
        (_2TupleS) bound 2-tuple. Return None if input is None
    """

    if p_2tupleT_S is None:
        return None

    bound_2tuple_S_list: List[_2Tuple] = []
    bound_2tuple_map: set = set()
    for cur_2tupleT in p_2tupleT_S.list():
        cur_bound_2tuple = get_bound_2tuple(cur_2tupleT)
        if cur_bound_2tuple.instance() not in bound_2tuple_map:
            bound_2tuple_S_list.append(_2Tuple(cur_bound_2tuple.list()))
            bound_2tuple_map.add(cur_bound_2tuple.instance())

    return _2TupleS(bound_2tuple_S_list)


def get_bound_2tuple(p_2tupleT: _2TupleT) -> _2Tuple | None:
    """
    (definition 19)Get the bound 2-tuple of a tuple of 2-tuples with a limited length.

    Args:
        p_2tupleT (_2TupleT): A _2TupleT instance with a limited length

    Returns:
        (_2Tuple): Bound 2-tuple
    """

    if p_2tupleT is None or len(p_2tupleT) == 0:
        return None

    min_first: object = p_2tupleT[0].first()
    max_second: object = p_2tupleT[0].second()

    for _2tuple in p_2tupleT.list():
        if min_first > _2tuple.first():
            min_first = _2tuple.first()
        if max_second < _2tuple.second():
            max_second = _2tuple.second()

    return _2Tuple([min_first, max_second])
