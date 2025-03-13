"""
@file _2Tuple.py
@brief: _2Tuple class.
@author: li.zhong.yuan@outlook.com
@date: 2025/2/6
"""


from simulation.base.structure import LiZhongYuanTuple


class _2Tuple(LiZhongYuanTuple):

    def first(self) -> any:
        """
        Get the first element of the tuple.

        Returns:
            (any) The first element
        """
        return self.__getitem__(0)


    def second(self) -> any:
        """
        Get the second element of the tuple.

        Returns:
            (any) The second element
        """
        return self.__getitem__(1)


    def instance(self) -> tuple[any, any]:
        """
        Get Python's native 2-tuple.

        Returns:
            (tuple[any, any]) Python's native 2-tuple
        """
        return self.__getitem__(0), self.__getitem__(1)

