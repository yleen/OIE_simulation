"""
@file complete_asc_order_filtered_2tuple_TS.py
@brief: Function for complete asc order filtered 2TupleTS instance.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/25
"""


from simulation.OIE._2Tuple_TS import _2TupleTS


def f_complete_asc_order_filtered_2tuple_TS(p_2tuple_TS: _2TupleTS) -> _2TupleTS:
    """
    (definition 22)Get the complete ascending order filtered subset of a 2TupleTS instance

    Args:
        p_2tuple_TS (_2TupleTS): A 2TupleTS instance

    Returns:
        (_2TupleTS): The complete ascending order filtered subset
    """

    if p_2tuple_TS.cardinality() < 2:
        return p_2tuple_TS

    sub_2tuple_TS: _2TupleTS = _2TupleTS()

    for _2tuple_T in p_2tuple_TS:
        is_complete_asc_order: bool = True
        for i in range(len(_2tuple_T) - 1):
            if _2tuple_T[i].second() > _2tuple_T[i + 1].first():
                is_complete_asc_order = False
                break
        if is_complete_asc_order:
            sub_2tuple_TS.add(_2tuple_T)

    return sub_2tuple_TS
