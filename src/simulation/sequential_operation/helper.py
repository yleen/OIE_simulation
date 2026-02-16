"""
@file helper.py
@brief: helper functions.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/14
"""


from typing import Tuple, Any

from simulation.base.structure import TwoTupleTS
from simulation.oie.event_star import EventStarS
from simulation.oie.optional_intervals_event_set import OIES


def get_2tuple_from_2tupleTS(p_2tuple_TS: TwoTupleTS, p_idx: int, p_n: int) -> Tuple[Any, Any] | None:
    """
    Retrieve specific 2-tuple element from 2TupleTS collection
    Args:
        p_2tuple_TS (TwoTupleTS): A 2TupleTS instance
        p_idx (int): An index for elements of p_2tuple_TS
        p_n (int): An index for an element of p_2tuple_TS

    Returns:
        (_2Tuple | None): Get the p_n-th 2-tuple of the element at index p_idx in p_2tuple_TS. Return None if it doesn't exist.
    """

    if p_idx < 1 or p_idx > p_2tuple_TS.cardinality():
        return None
    if p_n < 1 or p_n > len(p_2tuple_TS[p_idx - 1]):
        return None
    return p_2tuple_TS[p_idx - 1][p_n - 1]


def check_idxT_border(p_idx_T: Tuple[int,...], length: int) -> bool:
    """
    Check the upper and lower bounds of the index tuple
    Args:
        p_idx_T (Tuple[int,...]): An index tuple
        length (int): The extent of the range

    Returns:
        bool: Whether the bound of p_idx_T is legal
    """

    for idx in p_idx_T:
        if not isinstance(idx, int) or idx < 1 or idx > length:
            return False
    return True


def has_duplicates(tup: Tuple) -> bool:
    """
    Check if there are identical elements in the tuple.

    Args:
        tup (Tuple): A tuple

    Returns:
        (bool) result
    """
    return len(set(tup)) != len(tup)


def gen_C(p_oieS: OIES, p_idxT):
    C_list = []
    for i in range(len(p_idxT)):
        C_list.append(p_oieS[p_idxT[i] - 1])
    return tuple(C_list)

def gen_A(p_oieS: OIES, p_idxT):
    A_list = []
    for i in range(len(p_idxT)):
        A_list = A_list + p_oieS[p_idxT[i] - 1].A().list()
    return EventStarS(*A_list)


def check_params(p_oieS: OIES, p_idxT):
    if len(p_oieS) != len(p_idxT):
        raise ValueError("The length of p_OIE_S must be equal to the length of p_idxT.")
    if not check_idxT_border(p_idxT, len(p_idxT)):
        raise ValueError("p_idxT error.")


def check_void_condition_validation(p_oieS: OIES) -> bool:
    if p_oieS.has_duplicated_instances():
        print(f"There are duplicate elements, return oie_void")
        return False
    if p_oieS.has_intersection_of_atomEventEstarS():
        print(f"There are duplicate AtomEvent* instances, return oie_void")
        return False
    if any(cur_oie.is_void() for cur_oie in p_oieS):
        print(f"There is at least one oie_void in p_oieS, return oie_void")
        return False
    return True


def print_finish_line() -> None:
    print(f"############################## Finish ##############################\n\n\n\n")
