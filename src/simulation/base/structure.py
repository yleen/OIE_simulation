"""
@file structure.py
@brief: LiZhongYuanSet & LiZhongYuanTuple.
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

    def __getitem__(self, index: int) -> Any:
        return self._list[index]

    def __setitem__(self, index, value):
        self._list[index] = value
        self._dict[index + 1] = value

    def __str__(self) -> str:
        format_str: str = "{"
        for i, elem in enumerate(self._list):
            if i < len(self._list) - 1:
                format_str += (str(elem) + ", ")
            else:
                format_str += str(elem)
        format_str += "}"
        return format_str

    def __eq__(self, other):
        if len(self._list) != other.cardinality():
            return False
        for item in self._list:
            cur_equal = False
            for other_item in other:
                if item == other_item:
                    cur_equal = True
                    break
            if not cur_equal:
                return False
        return True

    def __len__(self):
        return len(self._list)

    def get(self, p_i: int) -> Any:
        """
        Let set S = { a1, a2, a3, ..., an }, get an element with index number
        Args:
            p_i (int): index number
        Returns:
            (any): The element of the set with the index number p_i,
            if there is no such element in the set, return None
        """
        if p_i < 1 or p_i > len(self._list):
            return None
        return self._list[p_i - 1]

    def index(self, p_item) -> int | None :
        """
        Let set S = { a1, a2, a3, ..., an }, input an item, get its index
        Args:
            p_item: an input value
        Returns:
           (int | None): index of p_item, if there is no such element in the set, return None
        """
        for i in range(1, len(self._list) + 1):
            if self._list[i - 1] == p_item:
                return i
        return None

    def dict(self):
        return self._dict

    def cardinality(self) -> int:
        return len(self._list)

    def list(self) -> List[Any]:
        return self._list

    def empty(self) -> bool:
        return len(self._list) == 0

    def has(self, item: Any) -> bool:
        for elem in self._list:
            if item == elem:
                return True
        return False

    def add(self, elem):
        if self.has(tuple(elem)):
            return
        self._list.append(tuple(elem))


class TwoTupleS(LiZhongYuanSet):
    pass


class TwoTupleSS(LiZhongYuanSet):
    pass


class TwoTupleTS(LiZhongYuanSet):
    pass


