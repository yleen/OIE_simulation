"""
@file infeasible.py
@brief Functions for unfeasible items.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""


from typing import Any, List, Tuple, Dict
from simulation.base.structure import TwoTupleTS


def get_custom_wildcard_matched_infeasible_2tupleTS(p_idxT: Tuple[int,...],
                                                    p_wildcard_infeasible_2tupleTS: TwoTupleTS,
                                                    p_wildcard_infeasible_idxT: Tuple[int,...]) -> TwoTupleTS:
    """
    Get custom wildcard infeasible 2-tuple collection ordered by p_idxT
    Args:
        p_idxT (Tuple[int,...]): The index order tuple, { idx_1, idx_2, ..., idx_n }
        p_wildcard_infeasible_2tupleTS (TwoTupleTS): Source collection of wildcard invalid 2-tuples, { 2tupleT_1, 2tupleT_2, ..., 2tupleT_n }
        p_wildcard_infeasible_idxT(Tuple[int,...]): The index tuple for source collection of wildcard invalid 2-tuples, { i1, i2, ..., in }
    Returns:
        (TwoTupleTS): Ordered collection of invalid 2-tuples.
    """
    # ---------- 1 Build tuple index conversion dictionary  ----------
    idx_trans_dict: Dict = {}
    for i in range(0, len(p_idxT)):
        for j in range(0, len(p_wildcard_infeasible_idxT)):
            if p_wildcard_infeasible_idxT[j] == p_idxT[i]:
                idx_trans_dict[j] = i
    # ---------- 2 Build wildcard infeasible 2-tuple collection under the order of p_idxT ----------
    custom_wildcard_infeasible_2tupleTS: TwoTupleTS = TwoTupleTS()
    for infeasible_2tupleT in p_wildcard_infeasible_2tupleTS:
        # 2.1 Gen custom_wildcard_infeasible_2tupleT, add to custom_wildcard_infeasible_2tupleT_list
        custom_wildcard_infeasible_2tuple_list: List[Tuple[Any, Any]] = []
        for j in range(0, len(p_wildcard_infeasible_idxT)):
            i: int = idx_trans_dict[j]
            custom_wildcard_infeasible_2tuple: Tuple[Any, Any] = infeasible_2tupleT[i]
            custom_wildcard_infeasible_2tuple_list.append(custom_wildcard_infeasible_2tuple)
        # 2.2 Add custom_wildcard_infeasible_2tupleT_list to custom_wildcard_infeasible_2tupleTS
        custom_wildcard_infeasible_2tupleTS.add(custom_wildcard_infeasible_2tuple_list)
    # ---------- 3 return result ----------
    return custom_wildcard_infeasible_2tupleTS

