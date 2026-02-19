"""
@file feasible.py
@brief Functions for feasible sub set.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""
from simulation.base.structure import TwoTupleTS, TwoTupleSS
from simulation.base.helper import is_wildcard_matched
from simulation.oie.optional_intervals_event_set import OIES


def remove_infeasible_elements_from_2tupleTS(p_2tupleTS: TwoTupleTS,
                                             p_wildcard_infeasible_2tupleTS: TwoTupleTS) -> TwoTupleTS:
    """
    Remove the infeasible elements from an instance of 2TupleTS instance.
    Args:
        p_2tupleTS (TwoTupleTS): An instance of 2TupleTS instance
        p_wildcard_infeasible_2tupleTS (TwoTupleTS): A wildcard infeasible 2TupleTS instance as pattern set.
    Returns:
        (TwoTupleTS): feasible 2TupleTS instance.
    """
    feasible_2tupleTS: TwoTupleTS = TwoTupleTS()
    for cur_2tupleT in p_2tupleTS:
        # Skip invalid cur_2tupleT in p_wildcard_unfeasible_2tupleTS
        if cur_2tupleT in p_wildcard_infeasible_2tupleTS:
            continue
        # cur_2tupleT is invalid if wildcard match exists in p_wildcard_unfeasible_2tupleTS
        wildcard_matched: bool = False
        for wildcard_infeasible_2tupleT in p_wildcard_infeasible_2tupleTS:
            if is_wildcard_matched(cur_2tupleT, wildcard_infeasible_2tupleT):
                wildcard_matched = True
                break
        if wildcard_matched:
            continue
        # cur_2tupleT is valid, add it into feasible_2tupleTS
        feasible_2tupleTS.add(cur_2tupleT)
    return feasible_2tupleTS


def get_feasible_2tupleTS_from_Nat_Iso_2_CP(p_oieS: OIES, p_idxT: tuple[int,...]) -> TwoTupleTS:
    """
    (definition 16) Get the feasible subset of the set that
    is naturally isomorphic to the Cartesian Product of all
    I(3rd elements) of members of a finite OIES instance in
    an index order
    Args:
        p_oieS (OIES): A finite OIES instance
        p_idxT (tuple[int,...]): An index order
    Returns:
        (TwoTupleTS): The feasible subset
    """
    wildcard_infeasible_2tupleTS: TwoTupleTS = p_oieS.get_custom_infeasible_2tupleTS(p_idxT=p_idxT)
    interval_2tupleSS: TwoTupleSS = p_oieS.get_interval_2tupleSS()
    Nat_Iso_2_CP_of_2tupleSS: TwoTupleTS = p_oieS.get_Nat_Iso_2_CP_of_interval_2tupleSS(p_interval_2tupleSS=interval_2tupleSS,
                                                                                        p_idxT=p_idxT)
    feasible_2tupleTS: TwoTupleTS = \
        remove_infeasible_elements_from_2tupleTS(p_2tupleTS=Nat_Iso_2_CP_of_2tupleSS,
                                                 p_wildcard_infeasible_2tupleTS=wildcard_infeasible_2tupleTS)
    return feasible_2tupleTS