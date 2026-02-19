"""
@file infeasible.py
@brief Functions for unfeasible items.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from typing import Any, List, Tuple
from simulation.base.structure import TwoTupleTS


def get_wildcard_matched_infeasible_2tupleTS(p_op_idxT: Tuple[Any,...],
                                             p_wildcard_infeasible_2tupleTS: TwoTupleTS,
                                             p_wildcard_infeasible_idxT: Tuple[Any,...]) -> TwoTupleTS:
    """
    todo 优化
    (definition 15) Unfeasible Intvl2TupleTS instance for all members of a OIES instance under a certain index order
    
    p_wildcard_unfeasible_Intvl_2tuple_TS = { _2tuple_T_1, _2tuple_T_2, ..., _2tuple_T_n }
    p_wildcard_unfeasible_Intvl_idx_T = { i1, i2, ..., in }, Specifies tuple index order for p_wildcard_unfeasible_Intvl_2tuple_TS elements
    p_op_idx_T = { idx_1, idx_2, ..., idx_n }
    Get wildcard-invalid Intvl 2-tuple collection ordered by p_op_idx_T
    Args:
        p_op_idxT: Index order tuple
        p_wildcard_infeasible_2tupleTS: Source collection of wildcard invalid Intvl 2-tuples
        p_wildcard_infeasible_idxT: Source collection of wildcard invalid Intvl 2-tuples index

    Returns:
        (TwoTupleTS): Ordered collection of invalid 2-tuples.
    """

    # ---------- 1 Build tuple index conversion dictionary  ----------

    idx_trans_dict: dict = {}
    for op_idx_pos in range(0, len(p_op_idxT)):
        for i in range(0, len(p_wildcard_infeasible_idxT)):
            if p_wildcard_infeasible_idxT[i] == p_op_idxT[op_idx_pos]:
                idx_trans_dict[i] = op_idx_pos

    # ---------- 2 Build wildcard invalid Intvl 2-tuple collection following p_op_idx_T order----------

    op_ordered_wildcard_infeasible_2tupleTS: TwoTupleTS = TwoTupleTS()
    for infeasible_2tupleT in p_wildcard_infeasible_2tupleTS:

        # 2.1
        # Convert wildcard_unfeasible_Intvl_2tuple_T to op_ordered_wildcard_unfeasible_Intvl_2tuple_T
        # following p_op_idx_T order based on expression operands' sequence
        op_ordered_wildcard_infeasible_2tuple_list: List[Tuple[Any, Any]] = []
        for i in range(0, len(p_wildcard_infeasible_idxT)):
            op_idx_pos: int = idx_trans_dict[i]
            wildcard_infeasible_2tuple: Tuple[Any, Any] = infeasible_2tupleT[op_idx_pos]
            op_ordered_wildcard_infeasible_2tuple_list.append(wildcard_infeasible_2tuple)

        # 2.2
        # op_ordered_wildcard_unfeasible_Intvl_2tuple_T add to op_ordered_wildcard_infeasible_2tupleTS
        op_ordered_wildcard_infeasible_2tupleTS.add(op_ordered_wildcard_infeasible_2tuple_list)

    # ---------- 3 return result ----------

    return op_ordered_wildcard_infeasible_2tupleTS

