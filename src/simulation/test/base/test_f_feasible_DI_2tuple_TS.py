"""
@file test_f_feasible_Intvl_2tuple_TS.py
@brief: Test cases of function f_feasible_Intvl_2tuple_TS.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from simulation.OIE.feasible import f_feasible_Intvl_2tuple_TS
from simulation.OIE.optional_intervals_event_set import OIES
from simulation.OIE.optional_intervals_event import AtomOIE
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE._2Tuple_S import _2TupleS


def test_f_feasible_Intvl_2tuple_TS() -> None:

    print('test_f_feasible_Intvl_2tuple_TS')

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    Intvl_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1', p_Intvl_2tuple_S=Intvl_2tuple_S_1)

    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])
    Intvl_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2', p_Intvl_2tuple_S=Intvl_2tuple_S_2)

    OIE_S_1 = OIES([ atom_OIE_1, atom_OIE_2 ])
    unfeasible_Intvl_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # unfeasible_Intvl_2tuple_TS_1 = _2TupleTS([
    #     _2TupleT([ '*', '*' ])
    # ])

    OIE_S_1.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_1,
                                                    p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    feasible_Intvl_2tuple_TS = f_feasible_Intvl_2tuple_TS(OIE_S_1, (1, 2))

    print(feasible_Intvl_2tuple_TS)
