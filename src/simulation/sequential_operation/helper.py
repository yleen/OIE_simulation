"""
@file helper.py
@brief: helper functions.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/14
"""

from typing import Tuple, Any, List
from simulation.base.structure import TwoTupleTS, TwoTupleS
from simulation.oie.event_star import EventStarS, EventStar
from simulation.oie.optional_intervals_event import OIE
from simulation.oie.optional_intervals_event_set import OIES
from test.instance import oie_void


def get_2tuple_from_2tupleTS(p_2tupleTS: TwoTupleTS, p_idx: int, p_n: int) -> Tuple[Any, Any] | None:
    """
    Retrieve specific 2-tuple element from 2TupleTS collection
    Args:
        p_2tupleTS (TwoTupleTS): A 2TupleTS instance
        p_idx (int): An index for elements of p_2tuple_TS
        p_n (int): An index for an element of p_2tuple_TS
    Returns:
        (Tuple[Any, Any] | None): Get the p_n-th 2-tuple of the element at index p_idx in p_2tuple_TS. Return None if it doesn't exist.
    """
    if p_idx < 1 or p_idx > p_2tupleTS.cardinality():
        return None
    if p_n < 1 or p_n > len(p_2tupleTS[p_idx - 1]):
        return None
    return p_2tupleTS[p_idx - 1][p_n - 1]


# def check_idxT_border(p_idxT: Tuple[int,...], length: int) -> bool:
def check_idxT_border(p_idxT: Tuple[int,...], p_lower_limit: int, p_upper_limit: int) -> bool:
    """
    Check the upper and lower bounds of the index tuple
    Args:
        p_idxT (Tuple[int,...]): An index tuple
        p_upper_limit (int): The upper limit
        p_lower_limit (int): The lower limit
    Returns:
        (bool): Whether all indices are valid
    """

    for idx in p_idxT:
        if not isinstance(idx, int) or idx < p_lower_limit or idx > p_upper_limit:
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


def gen_C(p_oieS: OIES, p_idxT: Tuple[int,...]) -> tuple[OIE,...]:
    C_list: List[OIE] = []
    for i in range(len(p_idxT)):
        C_list.append(p_oieS[p_idxT[i] - 1])
    return tuple(C_list)


def gen_A(p_oieS: OIES, p_idxT: Tuple[int,...]) -> EventStarS:
    A_list: List[EventStar] = []
    for i in range(len(p_idxT)):
        A_list = A_list + p_oieS[p_idxT[i] - 1].A().list()
    return EventStarS(*A_list)


def check_params(p_oieS: OIES, p_idxT: Tuple[int,...]) -> None:
    if len(p_oieS) != len(p_idxT):
        raise ValueError("The length of p_OIE_S must be equal to the length of p_idxT.")
    if not check_idxT_border(p_idxT=p_idxT, p_lower_limit=1, p_upper_limit=len(p_idxT)):
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


def get_min_1st_of_2tupleS(p_2tupleS: TwoTupleS) -> float:
    if p_2tupleS.empty():
        raise ValueError("p_2tupleS is empty.")
    return min(cur_2tuple[0] for cur_2tuple in p_2tupleS)


def get_max_2nd_of_2tupleS(p_2tupleS: TwoTupleS) -> float:
    if p_2tupleS.empty():
        raise ValueError("p_2tupleS is empty.")
    return max(cur_2tuple[1] for cur_2tuple in p_2tupleS)


def get_common_left_boundary_of_2tupleTS(p_oieS: OIES) -> float:
    if p_oieS.empty():
        raise ValueError("p_oieS is empty.")
    for cur_oie in p_oieS:
        if cur_oie == oie_void:
            raise ValueError("cur_oie is oie_void.")
    cur_common_left_boundary: float = get_min_1st_of_2tupleS(p_oieS[0].I())
    for cur_oie in p_oieS:
        if cur_common_left_boundary != get_min_1st_of_2tupleS(cur_oie.I()):
            raise ValueError("The left boundary of the interval set is not the same.")
    return cur_common_left_boundary


def get_common_right_boundary_of_2tupleTS(p_oieS: OIES) -> float:
    if p_oieS.empty():
        raise ValueError("p_oieS is empty.")
    for cur_oie in p_oieS:
        if cur_oie == oie_void:
            raise ValueError("cur_oie is oie_void.")
    cur_common_right_boundary: float = get_max_2nd_of_2tupleS(p_oieS[0].I())
    for cur_oie in p_oieS:
        if cur_common_right_boundary != get_max_2nd_of_2tupleS(cur_oie.I()):
            raise ValueError("The right boundary of the interval set is not the same.")
    return cur_common_right_boundary


def print_finish_line() -> None:
    print(f"############################## Finish ##############################\n\n\n\n")
