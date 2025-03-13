"""
@file test_2TupleT.py
@brief: Test cases of _2TupleT.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import (_2TupleT,
                                        f_min_1_of_2tuple_T,
                                        f_max_2_of_2tuple_T)


def test_2TupleT():

    _2tuple_1 = _2Tuple([1, 2])
    _2tuple_2 = _2Tuple([3, 4])
    _2tuple_3 = _2Tuple([1, 3])
    _2tuple_4 = _2Tuple([2, 4])


    _2tuple_T_1 = _2TupleT([_2tuple_1, _2tuple_2])
    _2tuple_T_2 = _2TupleT([_2tuple_3, _2tuple_4])

    min_1st_of_1 = f_min_1_of_2tuple_T(_2tuple_T_1)
    max_2nd_of_1 = f_max_2_of_2tuple_T(_2tuple_T_1)
    min_1st_of_2 = f_min_1_of_2tuple_T(_2tuple_T_2)
    max_2nd_of_2 = f_max_2_of_2tuple_T(_2tuple_T_2)

    print(f'min_1st_of_1: {min_1st_of_1}')
    print(f'max_2nd_of_1: {max_2nd_of_1}')
    print(f'min_1st_of_2: {min_1st_of_2}')
    print(f'max_2nd_of_2: {max_2nd_of_2}')

    wildcard_2tuple_T = _2TupleT([_2tuple_1, '*'])
    print(_2tuple_T_1.is_wildcard_included(wildcard_2tuple_T))
    print(_2tuple_T_2.is_wildcard_included(wildcard_2tuple_T))
