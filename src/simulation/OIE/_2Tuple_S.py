"""
@file _2TupleS.py
@brief: _2TupleS class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from simulation.base.structure import LiZhongYuanSet


class _2TupleS(LiZhongYuanSet):
     pass


def f_min_1_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    """
    (definition 6) Get the minimum first item of a 2TupleS instance.
    Args:
        p_2tuple_S (_2TupleSS): A 2TupleS instance

    Returns:
        (object): The minimum first item
    """
    min_first: object = None
    for item in p_2tuple_S:
        if min_first is None or min_first > item.first():
            min_first = item.first()
    return min_first


def f_max_2_of_2tuple_S(p_2tuple_S: _2TupleS) -> object:
    """
    (definition 6) Functions for finding the minimum 1st item and the maximum 2nd item of a 2TupleS Instance)

    Args:
        p_2tuple_S (_2TupleSS):

    Returns:
        (object):
    """

    max_second: object = None
    for item in p_2tuple_S:
        if max_second is None or max_second < item.second():
            max_second = item.second()
    return max_second