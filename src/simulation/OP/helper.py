"""
@file helper.py
@brief: helper functions.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/14
"""


from typing import Tuple
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_TS import _2TupleTS


def get_2tuple_from_2tuple_TS(p_2tuple_TS: _2TupleTS, p_idx: int, p_n: int) -> _2Tuple | None:
    """
    Retrieve specific 2-tuple element from 2TupleTS collection
    Args:
        p_2tuple_TS (_2TupleTS): A 2TupleTS instance
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


def check_idx_tuple_border(p_idx_T: Tuple[int,...], length: int) -> bool:
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


def print_finish_line() -> None:
    print(f"############################## Finish ##############################\n\n\n\n")
