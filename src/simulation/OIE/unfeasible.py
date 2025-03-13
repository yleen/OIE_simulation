"""
@file unfeasible.py
@brief Functions for unfeasible items.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from typing import Any, List
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_TS import _2TupleTS


def get_custom_ordered_wildcard_unfeasible_2tuple_TS(p_op_idx_T: tuple[Any,...],
                                                     p_wildcard_unfeasible_2tuple_TS: _2TupleTS,
                                                     p_wildcard_unfeasible_idx_T: tuple[Any,...]) -> _2TupleTS:
    """
    todo 优化
    (definition 15) Unfeasible Intvl2TupleTS instance for all members of a OIES instance under a certain index order
    
    p_wildcard_unfeasible_Intvl_2tuple_TS = { _2tuple_T_1, _2tuple_T_2, ..., _2tuple_T_n }
    p_wildcard_unfeasible_Intvl_idx_T = { i1, i2, ..., in }, Specifies tuple index order for p_wildcard_unfeasible_Intvl_2tuple_TS elements
    p_op_idx_T = { idx_1, idx_2, ..., idx_n }
    Get wildcard-invalid Intvl 2-tuple collection ordered by p_op_idx_T
    Args:
        p_op_idx_T: Index order tuple 
        p_wildcard_unfeasible_2tuple_TS: Source collection of wildcard invalid Intvl 2-tuples
        p_wildcard_unfeasible_idx_T: Source collection of wildcard invalid Intvl 2-tuples index

    Returns:
        (_2TupleTS): Ordered collection of invalid 2-tuples.
    """

    # ---------- 1 Build tuple index conversion dictionary  ----------

    idx_trans_dict: dict = {}
    for op_idx_pos in range(0, len(p_op_idx_T)):
        for Intvl_pos in range(0, len(p_wildcard_unfeasible_idx_T)):
            if p_wildcard_unfeasible_idx_T[Intvl_pos] == p_op_idx_T[op_idx_pos]:
                idx_trans_dict[Intvl_pos] = op_idx_pos

    # ---------- 2 Build wildcard invalid Intvl 2-tuple collection following p_op_idx_T order----------

    op_ordered_wildcard_unfeasible_Intvl_2tuple_TS: _2TupleTS = _2TupleTS()
    for unfeasible_Intvl_2tuple_T in p_wildcard_unfeasible_2tuple_TS:

        # 2.1
        # Convert wildcard_unfeasible_Intvl_2tuple_T to op_ordered_wildcard_unfeasible_Intvl_2tuple_T
        # following p_op_idx_T order based on expression operands' sequence
        op_ordered_wildcard_unfeasible_Intvl_2tuple_list: List[_2Tuple] = []
        for Intvl_pos in range(0, len(p_wildcard_unfeasible_idx_T)):
            op_idx_pos: int = idx_trans_dict[Intvl_pos]
            wildcard_unfeasible_Intvl_2tuple: _2Tuple = unfeasible_Intvl_2tuple_T[op_idx_pos]
            op_ordered_wildcard_unfeasible_Intvl_2tuple_list.append(wildcard_unfeasible_Intvl_2tuple)

        op_ordered_unfeasible_Intvl_2tuple_T: _2TupleT = _2TupleT(op_ordered_wildcard_unfeasible_Intvl_2tuple_list)

        # 2.2
        # op_ordered_wildcard_unfeasible_Intvl_2tuple_T add to op_ordered_wildcard_unfeasible_Intvl_2tuple_TS
        op_ordered_wildcard_unfeasible_Intvl_2tuple_TS.add(op_ordered_unfeasible_Intvl_2tuple_T)

    # ---------- 3 return result ----------

    return op_ordered_wildcard_unfeasible_Intvl_2tuple_TS

