"""
@file _2TupleT.py
@brief: _2TupleT class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from simulation.base.structure import LiZhongYuanTuple


class _2TupleT(LiZhongYuanTuple):

    def is_wildcard_included(self, p_pattern_2tuple_T) -> bool:
        """
        Check if there is wildcard inclusion.

        Args:
            p_pattern_2tuple_T (_2TupleT): pattern, use '*' for wildcard

        Returns:
            (bool): result
        """

        if len(self._list) != len(p_pattern_2tuple_T):
            return False

        matching: bool = True
        for i in range(0, len(self._list)):
            if p_pattern_2tuple_T[i] != self._list[i] and p_pattern_2tuple_T[i] != '*':
                matching = False
                break

        return matching


def f_min_1_of_2tuple_T(p_2tupleT: _2TupleT) -> object:
    """
    (definition 17/function 1)Obtain the minimum 1st item of a 2TupleT instance

    Args:
        p_2tupleT (_2TupleT): An _2TupleT instance

    Returns:
        (object): the minimum 1st item
    """

    if p_2tupleT is None:
        return None

    min_1st: object = p_2tupleT[0].first()
    for _2tuple in p_2tupleT:
        if min_1st > _2tuple.first():
            min_1st = _2tuple.first()

    return min_1st


def f_max_2_of_2tuple_T(p_2tupleT: _2TupleT) -> object:
    """
    (definition 17/function 2)Obtain the maximum 2nd item of a 2TupleT instance

    Args:
        p_2tupleT (_2TupleT): An _2TupleT instance

    Returns:
        (object): the maximum 2nd item
    """

    if p_2tupleT is None:
        return None

    max_2nd: object = p_2tupleT[0].second()
    for _2tuple in p_2tupleT:
        if max_2nd < _2tuple.second():
            max_2nd = _2tuple.second()

    return max_2nd
