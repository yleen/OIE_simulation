"""
@file complete_sequential_multiplication.py
@brief Complete sequential multiplication.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from typing import Tuple

from simulation.OP.helper import (check_idx_tuple_border,
                                   has_duplicates,
                                   print_finish_line)
from simulation.OIE._2Tuple_S import _2TupleS
from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE.bound import get_bound_2tuple_S
from simulation.OIE.feasible import f_feasible_Intvl_2tuple_TS
from simulation.OIE.optional_intervals_event import (OIE,
                                                              ErrorOIE)
from simulation.OIE.optional_intervals_event_set import OIES
from simulation.OP.multiplication.complete_asc_order_filtered_sub_2tuple_TS import f_complete_asc_order_filtered_2tuple_TS


def complete_sequential_multiplication(p_OIE_S: OIES,
                                       p_opd_idx_T: Tuple[int,...]) -> OIE:
    """
    (definition 23)Complete sequential multiplication
    Args:
        p_OIE_S (OIES): A OIES instance
        p_opd_idx_T(Tuple[int,...]): Index order of operands

    Returns:
        OIE: The result of complete sequential multiplication
    """

    print(f"####################################################################")
    print(f"###############  Complete sequential multiplication  ###############")
    print(f"####################################################################\n")

    print(f"1 Check parameters and handle.\n")

    if len(p_OIE_S) != len(p_opd_idx_T):
        raise ValueError("The length of p_OIE_S must be equal to the length of p_opd_idx_T.")

    if not check_idx_tuple_border(p_opd_idx_T, len(p_opd_idx_T)):
        raise ValueError("p_opd_idx_T error.")

    if has_duplicates(p_opd_idx_T):
        print(f"There are duplicate elements, get OIE_error")
        OIE_result: OIE = ErrorOIE()
        print(f"{str(OIE_result)}\n")
        print_finish_line()
        return OIE_result

    for cur_OIE in p_OIE_S:
        if cur_OIE.is_error():
            print(f"There are OIE_errors in p_OIE_S, get OIE_error")
            OIE_result: OIE = ErrorOIE()
            print(f"{str(OIE_result)}\n")
            print_finish_line()
            return OIE_result

    print(f"2 Take the valid subset of the Cartesian product of all members of \nthe Intvl2TupleSS instance of p_OIE_S in the order of the indices\n specified by p_opd_idx_T.\n")

    feasible_Intvl_2tuple_TS: _2TupleTS = f_feasible_Intvl_2tuple_TS(p_OIE_S, p_opd_idx_T)
    if feasible_Intvl_2tuple_TS.empty():
        print(f"feasible_Intvl_2tuple_TS is empty, get OIE_error")
        OIE_result: OIE = ErrorOIE()
        print(f"{str(OIE_result)}\n")
        print_finish_line()
        return OIE_result

    print(f"feasible_Intvl_2tuple_TS: {str(feasible_Intvl_2tuple_TS)}\n")

    print(f"3 Filter the feasible_Intvl_2tuple_TS using the complete ascending \n order rule to obtain a set of tuples of 2-tuples.\n")
    complete_asc_order_filtered_Intvl_2tuple_TS: _2TupleTS = f_complete_asc_order_filtered_2tuple_TS(feasible_Intvl_2tuple_TS)
    if complete_asc_order_filtered_Intvl_2tuple_TS.empty():
        print(f"complete_asc_order_filtered_Intvl_2tuple_TS is empty, get OIE_error")
        OIE_result: OIE = ErrorOIE()
        print(f"{str(OIE_result)}\n")
        print_finish_line()
        return OIE_result

    print(f"complete_asc_order_filtered_Intvl_2tuple_TS: {str(complete_asc_order_filtered_Intvl_2tuple_TS)}\n")

    print(f"4 Use complete_asc_order_filtered_Intvl_2tuple_TS to calculate the set of \n interval 2-tuples of OIE_result.\n")

    Intvl_2tuple_S: _2TupleS = get_bound_2tuple_S(complete_asc_order_filtered_Intvl_2tuple_TS)

    print(f"Intvl_2tuple_S: {str(Intvl_2tuple_S)}\n")

    print(f"5 Build OIE_result.\n")

    meta_OIE_list: list[OIE] = []

    OIE_result_expression: str = ""

    for i in range(len(p_opd_idx_T)):
        meta_OIE_list.append(p_OIE_S[p_opd_idx_T[i] - 1])
        OIE_result_expression += p_OIE_S[p_opd_idx_T[i] - 1].getExpression()
        if i < len(p_opd_idx_T) - 1:
            OIE_result_expression += ' * '

    OIE_result: OIE = OIE(p_expression=OIE_result_expression,
                             p_is_error=False,
                             p_is_atom=False,
                             p_OP='*',
                             p_meta_OIE_T=tuple(meta_OIE_list),
                             p_meta_Intvl_2tuple_TS=complete_asc_order_filtered_Intvl_2tuple_TS,
                             p_Intvl_2tuple_S=Intvl_2tuple_S)
    print(f"OIE_result: {str(OIE_result)}\n")

    print_finish_line()

    return OIE_result
