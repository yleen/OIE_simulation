"""
@file cartesian_product.py
@brief: The recursive implementation of f_CP_of_2tuple_SS.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from typing import (Tuple,
                    List)
from simulation.OIE._2Tuple_S import _2TupleS
from simulation.OIE._2Tuple_SS import _2TupleSS
from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT


def f_CP_of_2tuple_SS(p_2tuple_SS: _2TupleSS,
                      p_opr_idx_T: Tuple[int,...]) -> _2TupleTS:
    """
    (definition 14) Obtain the Cartesian product of each element of a 2TupleSS instance according to a certain index order.\n
    Let set p_2tuple_SS = {
        p_2tuple_S_1, p_2tuple_S_2, p_2tuple_S_3, ... , p_2tuple_S_n
    },
    and p_idx_T = [
        p_idx_1, p_idx_2, p_idx_3, ..., p_idx_n
    ]. \n
    get cartesian product with expression
        p_2tuple_S_(p_idx_1) * p_2tuple_S_(p_idx_2) * p_2tuple_S_(p_idx_3) * ... * p_2tuple_S_(p_idx_n)

    Args:
        p_2tuple_SS (_2TupleSS): A 2TupleSS instance(A set whose elements are sets of 2-tuples)
        p_opr_idx_T (Tuple[int,...]): A tuple representing the index order of operands

    Returns:
        (_2TupleTS): cartesian product(A 2TupleTS instance)
    """

    _2tuple_list_list: List[List[_2Tuple]] = \
        get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS=p_2tuple_SS,
                                                 p_opr_idx_T=p_opr_idx_T,
                                                 p_starting_pivot=1)

    _2tuple_T_list: List[_2TupleT] = []
    for _2tuple_list in _2tuple_list_list:
        _2tuple_T = _2TupleT(_2tuple_list)
        _2tuple_T_list.append(_2tuple_T)

    _2tuple_TS: _2TupleTS = _2TupleTS(_2tuple_T_list)

    return _2tuple_TS


def get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS: _2TupleSS,
                                             p_opr_idx_T: Tuple[int,...],
                                             p_starting_pivot: int) -> List[List[_2Tuple]]:
    """
    Obtain the Cartesian product of all members of a 2TupleSS instance starting from a certain index number and in a certain index order.\n
    Args:
        p_2tuple_SS (_2TupleSS): A set whose elements are sets of 2-tuples
        p_opr_idx_T (Tuple[any,...]): A tuple representing the index order of operands
        p_starting_pivot (int): The index number of the first element in p_opr_idx_T for the Cartesian product operation

    Returns (List[List[_2Tuple]]):
        The representation of the Cartesian product result in the form of List[List[_2Tuple]]
    """

    # Get cur_2tuple_S using p_starting_pivot from p_2tuple_SS
    cur_starting_idx: int = p_opr_idx_T[p_starting_pivot - 1] - 1
    cur_2tuple_S: _2TupleS = p_2tuple_SS[cur_starting_idx]

    # init recursion list
    cur_2tuple_list_list: List[List[_2Tuple]] = []

    # end recursion, construct result by cur_2tuple_S, return result
    if p_starting_pivot == len(p_opr_idx_T):
        for _2tuple in cur_2tuple_S:
                cur_2tuple_list_list.append([ _2tuple ])
        return cur_2tuple_list_list

    # Get the next pass of recursion: post_2tuple_list_list
    post_2tuple_list_list: List[List[_2Tuple]] = \
        get_custom_ordered_CP_of_2tuple_SS_recur(p_2tuple_SS=p_2tuple_SS,
                                                 p_opr_idx_T=p_opr_idx_T,
                                                 p_starting_pivot=p_starting_pivot + 1)

    # Construct result by post_2tuple_list_list and cur_2tuple_S
    for _2tuple in cur_2tuple_S:
        for post_2tuple_list in post_2tuple_list_list:
            _2tuple_list: List[_2Tuple] = [ _2tuple ] + post_2tuple_list
            cur_2tuple_list_list.append(_2tuple_list)

    return cur_2tuple_list_list
