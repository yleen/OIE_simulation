"""
@file naturally_isomorphic_to_cartesian_product.py
@brief: The recursive implementation of f_CP_of_2tuple_SS.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from typing import Tuple, List, Any
from simulation.base.structure import TwoTupleSS, TwoTupleTS, TwoTupleS


def get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS(p_2tupleSS: TwoTupleSS,
                                                               p_idxT: Tuple[int,...]) -> TwoTupleTS:
    """
    (definition 14) Get the naturally isomorphic to Cartesian product of each element of a 2TupleSS instance according to a certain index order.\n
    Let set p_2tupleSS = {
        2tupleS_1, 2tupleS_2, 2tupleS_3, ... , 2tupleS_n
    },
    and p_idx_T = [
        idx_1, idx_2, idx_3, ..., idx_n
    ]. \n
    get naturally isomorphic to cartesian product with expression
        2tupleS_(idx_1) * 2tupleS_(idx_2) * 2tupleS_(idx_3) * ... * 2tupleS_(idx_n)
    Args:
        p_2tupleSS (TwoTupleSS): A 2TupleSS instance
        p_idxT (Tuple[int,...]): A tuple representing the index order of operands
    Returns:
        (TwoTupleTS): the naturally isomorphic to cartesian product(A 2TupleTS instance)
    """
    twoTuple_list_list: List[List[Tuple[Any, Any]]] = get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS_recur(p_2tupleSS=p_2tupleSS,
                                                                                                                       p_idxT=p_idxT,
                                                                                                                       p_starting_pivot=1)
    return TwoTupleTS(*twoTuple_list_list)


def get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS_recur(p_2tupleSS: TwoTupleSS,
                                                                     p_idxT: Tuple[int,...],
                                                                     p_starting_pivot: int) -> List[List[Tuple[Any, Any]]]:
    """
    Get the naturally isomorphic to Cartesian product of each element of a 2TupleSS instance according to a certain index order recursively
    Args:
        p_2tupleSS (TwoTupleSS): A TwoTupleSS instance
        p_idxT (Tuple[any,...]): A tuple representing the index order of operands
        p_starting_pivot (int): The index number of the first element in p_idxT for the naturally isomorphic to Cartesian Product operation
    Returns (List[List[_2Tuple]]):
        The representation of the Cartesian product result in the form of List[List[_2Tuple]]
    """
    # Get cur_2tupleS using p_starting_pivot from p_2tupleSS
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
        get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS_recur(p_2tupleSS=p_2tupleSS,
                                                                         p_idxT=p_idxT,
                                                                         p_starting_pivot=p_starting_pivot + 1)

    # Construct result by post_2tuple_list_list and cur_2tupleS
    for cur_2tuple in cur_2tupleS:
        for post_2tuple_list in post_2tuple_list_list:
            cur_2tuple_list: List[Tuple[Any, Any]] = [ cur_2tuple ] + post_2tuple_list
            twoTuple_list_list.append(cur_2tuple_list)

    return twoTuple_list_list
