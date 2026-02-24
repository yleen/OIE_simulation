"""
@file first_type.py
@brief: The 1st type of implementation of an OIE instance
@author: li.zhong.yuan@outlook.com
@date: 2026/2/25
"""

from simulation.implement.helper import get_rand_2tuple
from simulation.optional_intervals_event.event import Event
from simulation.optional_intervals_event.optional_intervals_event import OIE


def first_type_implement(p_oie: OIE, p_event: Event) -> None:
    """
    (Definition 27) The 1st type of implementation of an OIE instance
    Args:
        p_oie (OIE): An OIE instance
        p_event (Event): An Event instance
    Returns:
        None
    """
    selected_2tuple = get_rand_2tuple(p_oie.I())
    p_event.set_starting_and_ending_timestamps(selected_2tuple[0], selected_2tuple[1])
