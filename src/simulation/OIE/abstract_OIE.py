"""
@file abstract_OIE.py
@brief: AbstractOIE class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""

from __future__ import annotations
from typing import Tuple
from sqlalchemy import BigInteger
from simulation.base.structure import TwoTupleS, TwoTupleTS, LiZhongYuanSet


class AbstractOIE:
    """
    An abstract class that defines the interface for oie
    """
    def C(self) -> Tuple[AbstractOIE]:
        pass

    def A(self) -> LiZhongYuanSet:
        pass

    def I(self) -> TwoTupleS:
        pass

    def F(self) -> TwoTupleTS:
        pass

    def get_id(self) -> BigInteger:
        pass

    def get_expr(self) -> str:
        pass
