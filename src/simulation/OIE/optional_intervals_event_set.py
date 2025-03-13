"""
@file optional_intervals_event_set.py
@brief: OIES & AtomOIES.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""


from typing import List, Tuple, Any
from simulation.OIE.abstract_OIE import AbstractOIE
from simulation.base.structure import LiZhongYuanSet
from simulation.OIE._2Tuple_SS import _2TupleSS
from simulation.OIE._2Tuple_TS import _2TupleTS
from simulation.OIE.cartesian_product import f_CP_of_2tuple_SS
from simulation.OIE.unfeasible import get_custom_ordered_wildcard_unfeasible_2tuple_TS


class OIES(LiZhongYuanSet):
    """
    OIE set class
    """

    def __init__(self, p_set_list: list):
        super().__init__(p_set_list)
        self._unfeasible_OIE_tuple = None
        self._wildcard_unfeasible_Intvl_2tuple_TS = None


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
            key: any = list(self._dict.keys())[i]
            dict_str += f"{key}: {self._dict[key].getExpression()}"
            if i != len(self._dict.keys()) - 1:
                dict_str += ", "
        dict_str += f" }}"

        return dict_str


    def get_dict_key(self, p_OIE: AbstractOIE) -> str | None:
        for key in list(self._dict.keys()):
            if self._dict[key] == p_OIE:
                return key
        return None


    def f_Intvl_2tuple_SS(self) -> _2TupleSS:
        """
        (definition 11)Get the "set composed of interval 2-tuple's sets" of itself

        Returns:
            (_2TupleSS): Set composed of interval 2-tuple's sets
        """

        Intvl_2tuple_SS: _2TupleSS = _2TupleSS()

        for item in self._list:
            Intvl_2tuple_SS.add(item.f_Intvl_2tuple_S())

        return Intvl_2tuple_SS


    def set_wildcard_unfeasible_Intvl_2tuple_info(self,
                                               p_wildcard_unfeasible_Intvl_2tuple_TS: _2TupleTS,
                                               p_OIE_tuple: Tuple[AbstractOIE,...]) -> None:
        """
        Set _wildcard_unfeasible_Intvl_2tuple_TS and _unfeasible_OIE_tuple.

        Args:
            (p_wildcard_unfeasible_Intvl_2tuple_TS): Wildcard unfeasible Intvl2TupleTS instance
            (p_OIE_tuple): A OIE instance tuple

        Returns:
            None
        """

        for _2tuple_T in p_wildcard_unfeasible_Intvl_2tuple_TS:
            if len(_2tuple_T) != len(p_OIE_tuple):
                raise ValueError(f"Wrong wildcard unfeasible Intvl 2tuple info")

            for i in range(len(_2tuple_T)):
                if _2tuple_T[i] == '*':
                    continue
                OIE: AbstractOIE = p_OIE_tuple[i]
                if _2tuple_T[i] not in OIE.f_Intvl_2tuple_S():
                    raise ValueError(f"Wrong wildcard unfeasible Intvl 2tuple info")

        self._wildcard_unfeasible_Intvl_2tuple_TS = p_wildcard_unfeasible_Intvl_2tuple_TS
        self._unfeasible_OIE_tuple = p_OIE_tuple


    def get_custom_ordered_CP_of_Intvl_2tuple_SS(self,
                                              p_Intvl_2tuple_SS: _2TupleSS,
                                              p_op_idx_T: Tuple[int,...] | None) -> _2TupleTS:
        """
        Compute Cartesian product of Intvl2TupleS for all elements in the set using operand index order p_op_idx_T.
        When p_op_idx_T is None, use default operand index order (1, 2, 3, ..., n)
        Args:
            p_Intvl_2tuple_SS: Input collection of Intvl2TupleS
            p_op_idx_T: Tuple specifying Cartesian product operand index order, or None

        Returns:
            _2TupleSS: Cartesian product result of all Intvl2TupleS elements
        """

        # ---------- 1 None handling and parameter validation----------

        default_idx_T: tuple[int,...] = tuple(range(1, len(self._list) + 1))
        if p_op_idx_T is None:
            p_op_idx_T = default_idx_T
        else:
            sorted_idx_T: Tuple[int,...] = tuple(sorted(p_op_idx_T))
            if sorted_idx_T != default_idx_T:
                raise ValueError("Wrong p_op_idx_T !")

        # ---------- 2 Get p_opr_idx order for expression operations, Cartesian product result of all Intvl2TupleS elements ----------

        _2tuple_TS: _2TupleTS = f_CP_of_2tuple_SS(p_2tuple_SS=p_Intvl_2tuple_SS,
                                                  p_opr_idx_T=p_op_idx_T)

        return _2tuple_TS


    def get_custom_ordered_wildcard_unfeasible_Intvl_2tuple_TS(self,
                                                            p_op_idx_T: tuple[Any,...]) -> _2TupleTS:
        """
        todo:
        Args:
            p_op_idx_T:

        Returns:

        """

        unfeasible_Intvl_idx_list: List[any] = []

        for unfeasible_OIE in self._unfeasible_OIE_tuple:
            cur_idx: any = self.get_dict_key(unfeasible_OIE)
            if cur_idx is None:
                return _2TupleTS()
            unfeasible_Intvl_idx_list.append(cur_idx)

        wildcard_unfeasible_Intvl_2tuple_TS: _2TupleTS \
            = get_custom_ordered_wildcard_unfeasible_2tuple_TS(p_op_idx_T=p_op_idx_T,
                                                               p_wildcard_unfeasible_2tuple_TS=self._wildcard_unfeasible_Intvl_2tuple_TS,
                                                               p_wildcard_unfeasible_idx_T=tuple(unfeasible_Intvl_idx_list))

        return wildcard_unfeasible_Intvl_2tuple_TS


class AtomOIES(OIES):
    pass
