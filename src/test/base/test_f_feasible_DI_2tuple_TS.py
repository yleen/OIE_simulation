"""
@file test_f_feasible_Intvl_2tuple_TS.py
@brief: Test cases of function f_feasible_Intvl_2tuple_TS.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from simulation.oie.feasible import get_feasible_2tupleTS
from simulation.oie.optional_intervals_event_set import OIES
from simulation.oie.optional_intervals_event import AtomOIE
from simulation.oie._2Tuple import _2Tuple
from simulation.base.TwoTupleT import _2TupleT
from simulation.oie.TwoTupleTS import TwoTupleTS
from bk.TwoTupleS import TwoTupleS


def test_f_feasible_Intvl_2tuple_TS() -> None:

    print('test_f_feasible_Intvl_2tuple_TS')

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    Intvl_2tuple_S_1 = TwoTupleS([_2_tuple_1, _2_tuple_2, _2_tuple_3])
    atom_OIE_1 = AtomOIE(p_expr='atomOIE1', p_I=Intvl_2tuple_S_1)

    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])
    Intvl_2tuple_S_2 = TwoTupleS([_2_tuple_4, _2_tuple_5, _2_tuple_6])
    atom_OIE_2 = AtomOIE(p_expr='atomOIE2', p_I=Intvl_2tuple_S_2)

    OIE_S_1 = OIES([ atom_OIE_1, atom_OIE_2 ])
    unfeasible_Intvl_2tuple_TS_1 = TwoTupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # unfeasible_Intvl_2tuple_TS_1 = _2TupleTS([
    #     _2TupleT([ '*', '*' ])
    # ])

    OIE_S_1.set_wildcard_infeasible_2tupleTS(p_wildcard_infeasible_2tupleTS=unfeasible_Intvl_2tuple_TS_1,
                                             p_oieT=(atom_OIE_1, atom_OIE_2))

    feasible_Intvl_2tuple_TS = get_feasible_2tupleTS(OIE_S_1, (1, 2))

    print(feasible_Intvl_2tuple_TS)
