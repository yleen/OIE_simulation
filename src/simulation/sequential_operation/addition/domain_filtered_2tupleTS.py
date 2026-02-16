"""
@file domain_filtered_2tupleTS.py
@brief Predicate & function for domain filtered sub 2TupleTS instance.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""
from typing import Tuple, List

from simulation.oie.TwoTupleTS import TwoTupleTS


def Pred_is_2tupleT_in_Domain(p_2tupleT: Tuple[Tuple[float, float]],
                              p_2tupleTS: TwoTupleTS,
                              p_left: float,
                              p_right: float) -> bool:
    """
    (definition 19/predicate)Determine whether a 2TupleT instance is a member of the domain-filtered subset of a 2TupleTS instance in a domain.

    Args:
        p_2tupleT (TwoTupleT): A 2TupleT instance
        p_2tupleTS (TwoTupleTS): A 2TupleTS instance
        p_left (float): The left border of a domain
        p_right (float): The right border of a domain

    Returns:
        (bool): The result of the determination
    """

    if not p_2tupleTS.has(p_2tupleT):
        return False
    for cur_2tuple in p_2tupleT:
        if cur_2tuple[0] < p_left or cur_2tuple[1] > p_right:
            return False
    return True


def f_domain_filtered_2tupleTS(p_2tupleTS: TwoTupleTS,
                               p_left: float,
                               p_right: float) -> TwoTupleTS:
    """
    (definition 18/function)Get the domain filtered subset of a 2TupleTS instance in a domain

    Args:
        p_2tupleTS (TwoTupleTS): A 2TupleTS instance
        p_left (object): The left border of a domain
        p_right (object): The right border of a domain

    Returns:
        (_2TupleTS): The domain filtered subset
    """

    domain_filtered_2tupleTS: TwoTupleTS = TwoTupleTS()
    tuple_len = 0
    # exists_1st_equal_to_left: bool = False
    # exists_2nd_equal_to_right: bool = False

    for cur_2tupleT in p_2tupleTS:
        if not Pred_is_2tupleT_in_Domain(cur_2tupleT, p_2tupleTS, p_left, p_right):
            continue
        tuple_len = len(cur_2tupleT)
        domain_filtered_2tupleTS.add(cur_2tupleT)

    left_matched_list: List[bool] = [False] * tuple_len
    right_matched_list: List[bool] = [False] * tuple_len

    for cur_2tupleT in domain_filtered_2tupleTS:
        for i in range(tuple_len):
            if left_matched_list[i] and right_matched_list[i]:
                continue
            if not left_matched_list[i] and cur_2tupleT[i][0] == p_left:
                left_matched_list[i] = True
            if not right_matched_list[i] and cur_2tupleT[i][1] == p_right:
                right_matched_list[i] = True

    for i in range(tuple_len):
        if not left_matched_list[i] or not right_matched_list[i]:
            return TwoTupleTS()

    return domain_filtered_2tupleTS
