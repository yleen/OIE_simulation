"""
@file test_2TupleTS.py
@brief: Test cases of _2TupleTS.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from simulation.OP.helper import get_2tuple_from_2tuple_TS
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_TS import _2TupleTS


def test_2TupleTS():

    _2tuple_1 = _2Tuple([1, 2])
    _2tuple_2 = _2Tuple([3, 4])
    _2tuple_T_1 = _2TupleT([_2tuple_1, _2tuple_2])

    _2tuple_3 = _2Tuple([1, 3])
    _2tuple_4 = _2Tuple([2, 4])
    _2tuple_T_2 = _2TupleT([_2tuple_3, _2tuple_4])

    _2tuple_5 = _2Tuple([1, 2])
    _2tuple_6 = _2Tuple([3, 4])
    _2tuple_7 = _2Tuple([4, 5])
    _2tuple_T_3 = _2TupleT([_2tuple_5, _2tuple_6, _2tuple_7])

    _2tuple_TS = _2TupleTS([_2tuple_T_1, _2tuple_T_2, _2tuple_T_3])

    _2tuple_11 = get_2tuple_from_2tuple_TS(_2tuple_TS, 1, 1)
    print(_2tuple_11)
    _2tuple_22 = get_2tuple_from_2tuple_TS(_2tuple_TS, 2, 2)
    print(_2tuple_22)
    _2tuple_33 = get_2tuple_from_2tuple_TS(_2tuple_TS, 3, 3)
    print(_2tuple_33)
    _2tuple_36 = get_2tuple_from_2tuple_TS(_2tuple_TS, 3, 6)
    print(_2tuple_36)
