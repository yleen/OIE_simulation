"""
@file optional_intervals_event.py
@brief: oie, OIES, AtomOIE, AtomOIES and VoidOIE
@author: li.zhong.yuan@outlook.com
@date: 2024/11/15
"""


from __future__ import annotations
from typing import Tuple
from sqlalchemy import BigInteger
from simulation.base.structure import TwoTupleTS, TwoTupleS
from simulation.oie.abstract_oie import AbstractOIE
from simulation.oie.event_star import EventStarS
from util.snowflake import gen_snowflake_id


class OIE(AbstractOIE):
    """
    oie class
    """
    def __init__(self,
                 p_expr: str | None,
                 p_C: Tuple[OIE,...],
                 p_F: TwoTupleTS,
                 p_I: TwoTupleS,
                 p_A: EventStarS) -> None:
        super().__init__()
        self._id: BigInteger | None = gen_snowflake_id()
        self._mapped_event_id: BigInteger | None = None
        self._expr: str = p_expr
        self._component_oie_tuple: Tuple[OIE,...] = p_C
        self._interval_combinations: TwoTupleTS = p_F
        self._intervals: TwoTupleS = p_I
        self._atomic_eventStarS: EventStarS = p_A

    def get_id(self) -> BigInteger:
        return self._id

    def set_mapping_event_id(self, p_event_id: BigInteger) -> None:
        self._mapped_event_id = p_event_id

    def __eq__(self, other) -> bool:
        return self.C() == other.C() and self.F() == other.F() and self.I() == other.I() and self.A() == other.A()

    def __str__(self) -> str:
        left_bracket: str = '( ' if len(self.C()) > 0 else '('
        right_bracket: str = ' )' if len(self.C()) > 0 else ')'
        format_str: str =\
            (f"{self._expr}, id:{self._id}\n"
             f"{{\n" +
             f"\t C: { left_bracket + ', '.join([f"{oie.get_expr()}(id:{oie.get_id()})" for oie in self.C()]) + right_bracket },\n" +
             f"\t F: { str(self.F()) },\n" +
             f"\t I: { str(self.I()) },\n" +
             f"\t A: { str(self.A()) }\n" +
             f"}}"
             )
        return format_str

    def get_expr(self) -> str | None:
        return self._expr

    def is_void(self) -> bool:
        return len(self.C()) == 0 and self.F().empty() and self.I().empty() and self.A().empty()

    def is_atom(self) -> bool:
        return len(self.C()) == 0 and not self.F().empty() and not self.I().empty() and not self.A().empty()

    def C(self) -> Tuple[OIE,...]:
        return self._component_oie_tuple

    def F(self) -> TwoTupleTS:
        return self._interval_combinations

    def I(self) -> TwoTupleS:
        return self._intervals

    def A(self) -> EventStarS:
        return self._atomic_eventStarS


class AtomOIE(OIE):
    pass


class CompOIE(OIE):
    pass


class VoidOIE(OIE):
    """
    Void oie class
    """
    def __init__(self) -> None:
        super().__init__(p_expr='void_oie',
                         p_C=(),
                         p_F=TwoTupleTS(),
                         p_I=TwoTupleS(),
                         p_A=EventStarS())
        self._id: None = None
