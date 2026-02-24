"""
@file second_type.py
@brief: The 2nd type of implementation of an OIE instance
@author: li.zhong.yuan@outlook.com
@date: 2026/2/25
"""

from typing import List

from simulation.implement.helper import get_rand_2tupleT
from simulation.optional_intervals_event.event import Event
from simulation.optional_intervals_event.optional_intervals_event import OIE


def second_type_implement(p_oie: OIE, p_events: List[Event]) -> None:
    """
    (Definition 28) The 2nd type of implementation of an OIE instance
    Args:
        p_oie (OIE): An OIE instance
        p_events (List[Event]): A list of Event instances
    Returns:
        None
    """
    selected_2tupleT = get_rand_2tupleT(p_oie.F())
    for p_event, selected_2tuple in zip(p_events, selected_2tupleT):
        p_event.set_starting_and_ending_timestamps(selected_2tuple[0], selected_2tuple[1])
