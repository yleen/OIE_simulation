"""
@file optional_intervals_event_set.py
@brief: OIES & AtomOIES.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from typing import List, Tuple, Any, Set, Dict
from simulation.oie.abstract_oie import AbstractOIE
from simulation.base.structure import LiZhongYuanSet, TwoTupleSS, TwoTupleTS
from simulation.oie.naturally_isomorphic_to_cartesian_product import get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS
from simulation.oie.event_star import EventStar
from simulation.oie.infeasible import get_custom_wildcard_matched_infeasible_2tupleTS


class OIES(LiZhongYuanSet):
    """
    oie set class
    """
    def __init__(self, *arg):
        super().__init__(*arg)
        self._infeasible_oieT = None
        self._wildcard_infeasible_2tupleTS = None

    def __str__(self):
        dict_str: str = self._get_dict_str()
        format_str: str = \
            (f"{{\n" +
             f"\tdict: {dict_str},\n" +
             f"}}"
             )
        return format_str

    def __len__(self):
        return len(self._list)

    def _get_dict_str(self) -> str:
        dict_str: str = f"{{ "
        for i in range(len(self._dict.keys())):
            key: Any = list(self._dict.keys())[i]
            dict_str += f"{key}: {self._dict[key].get_expr()}"
            if i != len(self._dict.keys()) - 1:
                dict_str += ", "
        dict_str += f" }}"
        return dict_str

    def get_dict_key(self, p_OIE: AbstractOIE) -> str | None:
        for key in list(self._dict.keys()):
            if self._dict[key] == p_OIE:
                return key
        return None

    def get_idx_of_oie(self, p_OIE: AbstractOIE):
        return next((idx for idx, oie in self._dict.items() if oie == p_OIE), None)

    def get_interval_2tupleSS(self) -> TwoTupleSS:
        """
        (definition 11)Get the set composed of the I(3rd elements) of all OIE instance members
        Returns:
            (TwoTupleSS): set composed of the I(3rd elements) of all OIE instance members
        """
        return TwoTupleSS(*(item.I() for item in self._list))

    def get_interval_atomEventStarS_list(self):
        return [oie.A() for oie in self.list()]

    def set_wildcard_infeasible_2tupleTS(self,
                                         p_wildcard_infeasible_2tupleTS: TwoTupleTS,
                                         p_oieT: Tuple[AbstractOIE,...]) -> None:
        """
        Set self._wildcard_infeasible_2tupleTS and self._infeasible_oieT.
        Args:
            p_wildcard_infeasible_2tupleTS (TwoTupleTS): A wildcard infeasible interval 2TupleTS instance
            p_oieT (Tuple[AbstractOIE,...]): A finite tuple of OIE instances
        Returns:
            (None)
        """
        for cur_2tupleT in p_wildcard_infeasible_2tupleTS:
            if len(cur_2tupleT) != len(p_oieT):
                raise ValueError(f"Wrong wildcard infeasible 2tuple info")
            for cur_2tuple, cur_oie in zip(cur_2tupleT, p_oieT):
                if cur_2tuple == '*':
                    continue
                if cur_2tuple not in cur_oie.I():
                    raise ValueError(f"Wrong wildcard unfeasible Intvl 2tuple info")
        self._wildcard_infeasible_2tupleTS = p_wildcard_infeasible_2tupleTS
        self._infeasible_oieT = p_oieT

    def get_Nat_Iso_2_CP_of_interval_2tupleSS(self,
                                              p_interval_2tupleSS: TwoTupleSS,
                                              p_idxT: Tuple[int,...] | None) -> TwoTupleTS:
        """
        Compute Cartesian product of Intvl2TupleS for all elements in the set using operand index order p_op_idx_T.
        When p_op_idx_T is None, use default operand index order (1, 2, 3, ..., n)
        Args:
            p_interval_2tupleSS: Input collection of Intvl2TupleS
            p_idxT: Tuple specifying Cartesian product operand index order, or None
        Returns:
            TwoTupleSS: Cartesian product result of all Intvl2TupleS elements
        """
        # ---------- 1 None handling and parameter validation----------
        default_idxT: tuple[int,...] = tuple(range(1, len(self._list) + 1))
        if p_idxT is None:
            p_idxT = default_idxT
        elif tuple(sorted(p_idxT)) != default_idxT:
            raise ValueError("Wrong p_idxT !")
        # ---------- 2 Get p_opr_idx order for expression operations, Cartesian product result of all Intvl2TupleS elements ----------
        return get_naturally_isomorphic_to_Cartesian_Product_for_2tupleSS(p_2tupleSS=p_interval_2tupleSS, p_idxT=p_idxT)


    def get_custom_infeasible_2tupleTS(self, p_idxT: Tuple[int,...]) -> TwoTupleTS:
        infeasible_oie_idx_list: List[any] = []
        for cur_oie in self._infeasible_oieT:
            cur_oie_idx: Any = self.get_dict_key(cur_oie)
            if cur_oie_idx is None:
                return TwoTupleTS()
            infeasible_oie_idx_list.append(cur_oie_idx)

        return get_custom_wildcard_matched_infeasible_2tupleTS(p_idxT=p_idxT,
                                                               p_wildcard_infeasible_2tupleTS=self._wildcard_infeasible_2tupleTS,
                                                               p_wildcard_infeasible_idxT=tuple(infeasible_oie_idx_list))


    def has_duplicated_instances(self) -> bool:
        expr_set: Set = set()
        for item in self._list:
            expr: str = item.get_expr()
            if expr in expr_set:
                return True
            expr_set.add(expr)
        return False


    def has_intersection_of_atomEventEstarS(self):
        twoTuple_map: Dict[EventStar, int] = {}
        for atomEventStarS in self.get_interval_atomEventStarS_list():
            for atomEventStar in atomEventStarS:
                if twoTuple_map.get(atomEventStar) == 1:
                    return True
                else:
                    twoTuple_map[atomEventStar] = 1
        return False


class AtomOIES(OIES):
    pass
