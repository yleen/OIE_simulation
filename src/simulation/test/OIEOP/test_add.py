"""
@file test_add.py
@brief Test cases of complete sequential addition.
@author li.zhong.yuan@outlook.com
@date 2025/1/27
"""


from simulation.OIE._2Tuple import _2Tuple
from simulation.OIE._2Tuple_T import _2TupleT
from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE._2Tuple_S import _2TupleS
from simulation.OP.addition.complete_sequential_addition import complete_sequential_addition
from simulation.OIE.optional_intervals_event import AtomOIE
from simulation.OIE.optional_intervals_event_set import OIES


def test_complete_sequential_addition_1():

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

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 5])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S,
                                            p_opd_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)


def test_complete_sequential_addition_2():

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

    Intvl_2tuple_S_3 = _2TupleS([ _2_tuple_1, _2_tuple_5 ])
    atom_OIE_3 = AtomOIE(p_expression='atomOIE3',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_3)

    # ---------- 2 Init a OIES instance ----------

    OIE_S_1 = OIES([ atom_OIE_1, atom_OIE_2 ])
    OIE_S_2 = OIES([ atom_OIE_1, atom_OIE_2, atom_OIE_3 ])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    unfeasible_Intvl_2tuple_TS_1 = _2TupleTS([
        _2TupleT([ _2_tuple_1, _2_tuple_4 ])
    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S_1.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_1,
                                                    p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple_A = _2Tuple([1, 4])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S_1,
                                            p_opd_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple_A)


def test_complete_sequential_addition_3():

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
    wildcard_unfeasible_Intvl_2tuple_TS = _2TupleTS([
        _2TupleT([ _2_tuple_1, '*', ]),
        _2TupleT([ _2_tuple_2, '*', ]),
        _2TupleT([ '*', _2_tuple_6, ]),

    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=wildcard_unfeasible_Intvl_2tuple_TS,
                                                  p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 5])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S,
                                            p_opd_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)


def test_complete_sequential_addition_4():

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
    empty_unfeasible_Intvl_2tuple_TS = _2TupleTS([])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=empty_unfeasible_Intvl_2tuple_TS,
                                                    p_OIE_tuple=(atom_OIE_1, atom_OIE_2))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S,
                                            p_opd_idx_T=(1, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)


def test_complete_sequential_addition_5():

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

    Intvl_2tuple_S_3 = _2TupleS([ _2_tuple_1, _2_tuple_5 ])
    atom_OIE_3 = AtomOIE(p_expression='atomOIE3',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_3)

    # ---------- 2 Init a OIES instance ----------

    OIE_S_2 = OIES([ atom_OIE_1, atom_OIE_2, atom_OIE_3 ])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    unfeasible_Intvl_2tuple_TS_123 = _2TupleTS([
        _2TupleT(['*', '*', '*']),
    ])
    # 3.2 Assign to the member value of OIE_S
    OIE_S_2.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=unfeasible_Intvl_2tuple_TS_123,
                                                    p_OIE_tuple=(atom_OIE_1, atom_OIE_2, atom_OIE_3))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S_2,
                                            p_opd_idx_T=(1, 2, 3),
                                            p_domain_filter_2tuple=domain_filter_2tuple)


def test_complete_sequential_addition_6():

    # ---------- 1 Init some OIE instances ----------

    _2_tuple_1 = _2Tuple([1, 2])
    _2_tuple_2 = _2Tuple([3, 4])
    _2_tuple_3 = _2Tuple([4, 5])
    _2_tuple_4 = _2Tuple([1, 3])
    _2_tuple_5 = _2Tuple([2, 4])
    _2_tuple_6 = _2Tuple([3, 5])

    Intvl_2tuple_S_1 = _2TupleS([_2_tuple_1, _2_tuple_2, _2_tuple_3])
    atom_OIE_1 = AtomOIE(p_expression='atomOIE1',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_1)

    Intvl_2tuple_S_2 = _2TupleS([_2_tuple_4, _2_tuple_5, _2_tuple_6])
    atom_OIE_2 = AtomOIE(p_expression='atomOIE2',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_2)

    Intvl_2tuple_S_3 = _2TupleS([_2_tuple_1, _2_tuple_5])
    atom_OIE_3 = AtomOIE(p_expression='atomOIE3',
                           p_Intvl_2tuple_S=Intvl_2tuple_S_3)

    # ---------- 2 Init a OIES instance ----------

    OIE_S = OIES([atom_OIE_1, atom_OIE_2, atom_OIE_3])

    # ---------- 3 Set UnfeasibleIntvl2TupleTS instance to the OIES instance ----------

    # 3.1 init a UnfeasibleIntvl2TupleTS instance
    empty_unfeasible_Intvl_2tuple_TS = _2TupleTS([])
    # 3.2 Assign to the member value of OIE_S
    OIE_S.set_wildcard_unfeasible_Intvl_2tuple_info(p_wildcard_unfeasible_Intvl_2tuple_TS=empty_unfeasible_Intvl_2tuple_TS,
                                                  p_OIE_tuple=(atom_OIE_1, atom_OIE_2, atom_OIE_3))

    # ---------- 4 Add ----------

    # 4.1 Init a DomainFilter2Tuple instance
    domain_filter_2tuple = _2Tuple([1, 4])
    # 4.2 Execute
    OIE_res = complete_sequential_addition(p_finite_OIE_S=OIE_S,
                                            p_opd_idx_T=(1, 3, 2),
                                            p_domain_filter_2tuple=domain_filter_2tuple)
