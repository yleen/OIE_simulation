"""
@file structure.py
@brief: basic structure of the simulation.
@author: li.zhong.yuan@outlook.com
@date: 2024/11/20
"""

from __future__ import annotations
from typing import List, Dict, Any


class LiZhongYuanSet:
    def __init__(self, *args) -> None:
        args_list: List = []
        if args is not None:
            args_list = list(args)
        self._list: List = args_list
        self._dict: Dict = {i: self._list[i - 1] for i in range(1, len(self._list) + 1)}

    def __getitem__(self, p_index: int) -> Any:
        return self._list[p_index]

    def __setitem__(self, p_index: int, p_value: object) -> None:
        self._list[p_index] = p_value
        self._dict[p_index + 1] = p_value

    def __str__(self) -> str:
        format_str: str = "{"
        for i, elem in enumerate(self._list):
            if i < len(self._list) - 1:
                format_str += (str(elem) + ", ")
            else:
                format_str += str(elem)
        format_str += "}"
        return format_str

    def __eq__(self, p_other: LiZhongYuanSet) -> bool:
        if len(self._list) != p_other.cardinality():
            return False
        return all(item in p_other for item in self._list)

    def __len__(self) -> int:
        return len(self._list)

    def dict(self) -> Dict:
        return self._dict

    def cardinality(self) -> int:
        return len(self._list)

    def list(self) -> List:
        return self._list

    def empty(self) -> bool:
        return len(self._list) == 0

    def has(self, item: Any) -> bool:
        return item in self._list

    def add(self, elem) -> None:
        if self.has(tuple(elem)):
            return
        self._list.append(tuple(elem))


class TwoTupleS(LiZhongYuanSet):
    pass


class TwoTupleSS(LiZhongYuanSet):
    pass


class TwoTupleTS(LiZhongYuanSet):
    pass

