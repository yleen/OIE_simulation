"""
@file event.py
@brief: Event class.
@author: li.zhong.yuan@outlook.com
@date: 2026/2/24
"""

from sqlalchemy import BigInteger
from util.snowflake import gen_snowflake_id


class Event:
    def __init__(self, p_name: str,
                 p_starting_timestamp: float | None = None,
                 p_ending_timestamp: float | None = None) -> None:
        self._name: str = p_name
        self._id: BigInteger = gen_snowflake_id()
        self._mapped_event_star_id: BigInteger | None = None
        if p_starting_timestamp is not None and p_ending_timestamp is not None:
            assert_order_of_two_timestamps(p_starting_timestamp, p_ending_timestamp)
        if p_starting_timestamp is None or p_ending_timestamp is None:
            self._starting_timestamp: float | None = p_starting_timestamp
            self._ending_timestamp: float | None = p_ending_timestamp

    def __str__(self) -> str:
        format_str: str = f"{self._name}(id:{self._id})"
        return format_str

    def get_id(self) -> BigInteger:
        return self._id

    def set_bijective_event_star_id(self, p_event_star_id: BigInteger) -> None:
        self._mapped_event_star_id = p_event_star_id

    def get_bijective_event_star_id(self) -> BigInteger:
        return self._mapped_event_star_id

    def set_starting_and_ending_timestamps(self, p_starting_timestamp: float, p_ending_timestamp: float):
        assert_order_of_two_timestamps(p_starting_timestamp, p_ending_timestamp)
        self._starting_timestamp = p_starting_timestamp
        self._ending_timestamp = p_ending_timestamp


def assert_order_of_two_timestamps(p_starting_timestamp: float, p_ending_timestamp: float) -> None:
    """
    (Property 3) Assert the order of two timestamps.
    Args:
        p_starting_timestamp (float): The starting timestamp.
        p_ending_timestamp (float): The ending timestamp.
    Returns:
        None
    """
    assert p_starting_timestamp < p_ending_timestamp

