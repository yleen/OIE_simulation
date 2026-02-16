"""
@file cartesian_product.py
@brief: The recursive implementation of f_CP_of_2tuple_SS.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from typing import Tuple, List, Any
from simulation.base.structure import TwoTupleSS, TwoTupleTS, TwoTupleS


def get_CP_of_2tupleSS(p_2tupleSS: TwoTupleSS,
                       p_idxT: Tuple[int,...]) -> TwoTupleTS:
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
        p_2tupleSS (TwoTupleSS): A 2TupleSS instance(A set whose elements are sets of 2-tuples)
        p_idxT (Tuple[int,...]): A tuple representing the index order of operands
    Returns:
        (TwoTupleTS): cartesian product(A 2TupleTS instance)
    """

    twoTuple_list_list: List[List[Tuple[Any, Any]]] = \
        get_CP_of_2tupleSS_recur(p_2tupleSS=p_2tupleSS,
                                 p_idxT=p_idxT,
                                 p_starting_pivot=1)
    return TwoTupleTS(*twoTuple_list_list)


def get_CP_of_2tupleSS_recur(p_2tupleSS: TwoTupleSS,
                             p_idxT: Tuple[int,...],
                             p_starting_pivot: int) -> List[List[Tuple[Any, Any]]]:
    """
    Obtain the Cartesian product of all members of a 2TupleSS instance starting from a certain index number and in a certain index order.\n
    Args:
        p_2tupleSS (TwoTupleSS): A set whose elements are sets of 2-tuples
        p_idxT (Tuple[any,...]): A tuple representing the index order of operands
        p_starting_pivot (int): The index number of the first element in p_opr_idx_T for the Cartesian product operation

    Returns (List[List[_2Tuple]]):
        The representation of the Cartesian product result in the form of List[List[_2Tuple]]
    """
    # Get cur_2tupleS using p_starting_pivot from p_2tuple_SS
    cur_starting_idx: int = p_idxT[p_starting_pivot - 1] - 1
    cur_2tupleS: TwoTupleS = p_2tupleSS[cur_starting_idx]

    # init recursion list
    twoTuple_list_list: List[List[Tuple[Any, Any]]] = []

    # end recursion, construct result by cur_2tupleS, return result
    if p_starting_pivot == len(p_idxT):
        for cur_2tuple in cur_2tupleS:
                twoTuple_list_list.append([ cur_2tuple ])
        return twoTuple_list_list

    # Get the next pass of recursion: post_2tuple_list_list
    post_2tuple_list_list: List[List[Tuple[Any, Any]]] = \
        get_CP_of_2tupleSS_recur(p_2tupleSS=p_2tupleSS,
                                 p_idxT=p_idxT,
                                 p_starting_pivot=p_starting_pivot + 1)

    # Construct result by post_2tuple_list_list and cur_2tupleS
    for cur_2tuple in cur_2tupleS:
        for post_2tuple_list in post_2tuple_list_list:
            cur_2tuple_list: List[Tuple[Any, Any]] = [ cur_2tuple ] + post_2tuple_list
            twoTuple_list_list.append(cur_2tuple_list)

    return twoTuple_list_list
