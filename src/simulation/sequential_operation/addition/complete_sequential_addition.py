"""
@file complete_sequential_addition.py
@brief Complete sequential addition.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from typing import Tuple
from simulation.base.helper import get_bound_2tupleS
from simulation.base.structure import TwoTupleS, TwoTupleTS
from simulation.oie.abstract_oie import AbstractOIE
from simulation.oie.event_star import EventStarS
from simulation.sequential_operation.helper import (print_finish_line,
                                                    check_params,
                                                    check_void_condition_validation,
                                                    gen_C,
                                                    gen_A)
from simulation.oie.feasible import get_feasible_2tupleTS_from_Nat_Iso_2_CP
from simulation.oie.optional_intervals_event import OIE, VoidOIE
from simulation.oie.optional_intervals_event_set import OIES
from simulation.sequential_operation.addition.domain_filtered_2tupleTS import f_domain_filtered_2tupleTS


def complete_sequential_addition(p_oieS: OIES,
                                 p_idxT: Tuple[int,...],
                                 p_domain_filtering_2tuple: Tuple[float, float]) -> OIE:
    """
    (definition 21)Complete sequential addition
    Args:
        p_oieS (OIES): A finite OIES instance
        p_idxT(Tuple[int,...]): Index order of operands
        p_domain_filtering_2tuple(Tuple[float, float]): A domain filtering 2Tuple instance
    Returns:
        (OIE): The result of complete sequential addition
    """

    print(f"####################################################################")
    print(f"##################  Complete sequential addition  ##################")
    print(f"####################################################################\n")

    print(f"1 Check parameters and handle.\n")

    check_params(p_oieS=p_oieS, p_idxT=p_idxT)

    if not check_void_condition_validation(p_oieS=p_oieS):
        print_finish_line()
        return VoidOIE()
    C: tuple[AbstractOIE,...] = gen_C(p_oieS=p_oieS, p_idxT=p_idxT)
    A: EventStarS = gen_A(p_oieS=p_oieS, p_idxT=p_idxT)

    oie_res_expr: str = build_addition_res_expr(p_oieS=p_oieS,
                                                p_idxT=p_idxT,
                                                p_domain_filtering_2tuple=p_domain_filtering_2tuple)

    feasible_2tupleTS: TwoTupleTS = get_feasible_2tupleTS_from_Nat_Iso_2_CP(p_oieS=p_oieS, p_idxT=p_idxT)
    if feasible_2tupleTS.empty():
        print_finish_line()
        return VoidOIE()

    F: TwoTupleTS = f_domain_filtered_2tupleTS(p_2tupleTS=feasible_2tupleTS,
                                               p_left=p_domain_filtering_2tuple[0],
                                               p_right=p_domain_filtering_2tuple[1])
    if F.empty():
        print_finish_line()
        return VoidOIE()

    I: TwoTupleS = get_bound_2tupleS(p_2tupleTS=F)

    oie_result: OIE = OIE(p_expr=oie_res_expr, p_C=C, p_F=F, p_I=I, p_A=A)
    print_finish_line()

    return oie_result


def build_addition_res_expr(p_oieS: OIES,
                            p_idxT: Tuple[int,...],
                            p_domain_filtering_2tuple: Tuple[float, float]) -> str:
    oie_res_expr: str = f"\u2295|_{p_domain_filtering_2tuple[0]}^{p_domain_filtering_2tuple[1]}("
    for i in range(len(p_idxT)):
        oie_res_expr += p_oieS[p_idxT[i] - 1].get_expr()
        if i < len(p_idxT) - 1:
            oie_res_expr += ', '
    oie_res_expr += f")"
    return oie_res_expr