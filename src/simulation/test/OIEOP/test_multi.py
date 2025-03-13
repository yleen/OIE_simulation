"""
@file test_multi.py
@brief Test cases of complete sequential multiplication.
@author li.zhong.yuan@outlook.com
@date 2025/1/28
"""


from simulation.OP.multiplication.complete_sequential_multiplication import complete_sequential_multiplication
from simulation.OIE.optional_intervals_event import AtomOIE
from simulation.OIE.optional_intervals_event_set import OIES
from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_S import _2TupleS
from simulation.OIE._2Tuple_TS import _2TupleTS


def test_complete_sequential_multiplication_1():

    # ---------- 1 Init some AtomOIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    Intvl_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_1)

    Intvl_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_2)

    # ---------- 2 Init a OIES instance ----------

    OIE_S = OIES([ atom_OIE_1, atom_OIE_2 ])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    unfeasible_Intvl_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_2,
                                                  p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Multi ----------

    OIE_res = complete_sequential_multiplication(p_OIE_S=OIE_S,
                                                  p_opd_idx_T=(1, 2))


def test_complete_sequential_multiplication_2():

    # ---------- 1 Init some OIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    Intvl_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_1)

    Intvl_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_2)

    # ---------- 2 Init a OIES instance ----------

    OIE_S = OIES([ atom_OIE_1, atom_OIE_2 ])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    unfeasible_Intvl_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_2,
                                                  p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Multi ----------

    OIE_res = complete_sequential_multiplication(p_OIE_S=OIE_S,
                                                  p_opd_idx_T=(2, 1))


def test_complete_sequential_multiplication_3():

    # ---------- 1 Init some OIE instances ----------

    _2_tuple_1 = _2Tuple([ 1, 2 ])
    _2_tuple_2 = _2Tuple([ 3, 4 ])
    _2_tuple_3 = _2Tuple([ 4, 5 ])
    _2_tuple_4 = _2Tuple([ 1, 3 ])
    _2_tuple_5 = _2Tuple([ 2, 4 ])
    _2_tuple_6 = _2Tuple([ 3, 5 ])

    Intvl_2tuple_S_1 = _2TupleS([ _2_tuple_1, _2_tuple_2, _2_tuple_3 ])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_1)

    Intvl_2tuple_S_2 = _2TupleS([ _2_tuple_4, _2_tuple_5, _2_tuple_6 ])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_2)

    # ---------- 2 Init a OIES instance ----------

    OIE_S = OIES([ atom_OIE_1, atom_OIE_2 ])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    unfeasible_Intvl_2tuple_TS_2 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ]),
        _2TupleT([ _2_tuple_1, _2_tuple_5 ]),
        _2TupleT([ _2_tuple_2, _2_tuple_4 ]),
    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_2,
                                                  p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Multi ----------

    OIE_res = complete_sequential_multiplication(p_OIE_S=OIE_S,
                                                  p_opd_idx_T=(1, 1))