"""
@file domain_filtered_sub_2tuple_TS.py
@brief Predicate & function for domain filtered sub 2TupleTS instance.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from simulation.OIE._2Tuple_T import (_2TupleT,
                                        f_min_1_of_2tuple_T,
                                        f_max_2_of_2tuple_T)
from simulation.OIE._2Tuple_TS import _2TupleTS


def Pred_is_2tuple_T_in_Domain(p_2tuple_TS: _2TupleTS,
                               p_2tuple_T: _2TupleT,
                               p_left: object,
                               p_right: object) -> bool:
    """
    (definition 18/predicate)Determine whether a 2TupleT instance is a member of the domain-filtered subset of a 2TupleTS instance in a domain.

    Args:
        p_2tuple_TS (_2TupleTS): A 2TupleTS instance
        p_2tuple_T (_2TupleT): A 2TupleT instance
        p_left (object): The left border of a domain
        p_right (object): The right border of a domain

    Returns:
        (bool): The result of the determination
    """

    if not p_2tuple_TS.has(p_2tuple_T):
        return False

    for item in p_2tuple_T:
        if item.first() < p_left or item.second() > p_right:
            return False

    return True


def f_domain_filtered_sub_2tuple_TS(p_2tuple_TS: _2TupleTS,
                                    p_left: object,
                                    p_right: object) -> _2TupleTS:
    """
    (definition 18/function)Get the domain filtered subset of a 2TupleTS instance in a domain

    Args:
        p_2tuple_TS (_2TupleTS): A 2TupleTS instance
        p_left (object): The left border of a domain
        p_right (object): The right border of a domain

    Returns:
        (_2TupleTS): The domain filtered subset
    """

    sub_2tuple_TS: _2TupleTS = _2TupleTS()
    exists_1st_equal_to_left: bool = False
    exists_2nd_equal_to_right: bool = False

    for _2tuple_T in p_2tuple_TS:
        if not Pred_is_2tuple_T_in_Domain(p_2tuple_TS, _2tuple_T, p_left, p_right):
            continue

        sub_2tuple_TS.add(_2tuple_T)

        if not exists_1st_equal_to_left and f_min_1_of_2tuple_T(_2tuple_T) == p_left:
            exists_1st_equal_to_left = True
        if not exists_2nd_equal_to_right and f_max_2_of_2tuple_T(_2tuple_T) == p_right:
            exists_2nd_equal_to_right = True

    if exists_1st_equal_to_left and exists_2nd_equal_to_right:
        return sub_2tuple_TS

    return _2TupleTS()
