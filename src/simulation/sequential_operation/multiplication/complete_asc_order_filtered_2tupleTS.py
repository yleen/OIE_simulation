"""
@file complete_asc_order_filtered_2tuple_TS.py
@brief: Function for complete asc order filtered 2TupleTS instance.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/25
"""

from simulation.base.structure import TwoTupleTS


def f_complete_asc_order_filtered_2tupleTS(p_2tupleTS: TwoTupleTS) -> TwoTupleTS:
    """
    (definition 21)Get the complete ascending order filtered subset of a 2TupleTS instance
    Args:
        p_2tupleTS (TwoTupleTS): A 2TupleTS instance
    Returns:
        (TwoTupleTS): The complete ascending order filtered subset
    """
    sub_2tupleTS: TwoTupleTS = TwoTupleTS()
    for cur_2tupleT in p_2tupleTS:
        is_complete_asc_order: bool = True
        for i in range(len(cur_2tupleT) - 1):
            if cur_2tupleT[i][1] > cur_2tupleT[i + 1][0]:
                is_complete_asc_order = False
                break
        if is_complete_asc_order:
            sub_2tupleTS.add(cur_2tupleT)
    return sub_2tupleTS
