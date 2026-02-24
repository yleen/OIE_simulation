
from typing import List

from simulation.implement.helper import get_rand_2tupleT
from simulation.optional_intervals_event.event import Event
from simulation.optional_intervals_event.optional_intervals_event import OIE


def second_type_implement(p_oie: OIE, p_events: List[Event]) -> None:
    selected_2tupleT = get_rand_2tupleT(p_oie.F())
    for p_event, selected_2tuple in zip(p_events, selected_2tupleT):
        p_event.set_starting_and_ending_timestamps(selected_2tuple[0], selected_2tuple[1])
