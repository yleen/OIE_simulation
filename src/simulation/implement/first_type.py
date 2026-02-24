from simulation.implement.helper import get_rand_2tuple
from simulation.optional_intervals_event.event import Event
from simulation.optional_intervals_event.optional_intervals_event import OIE


def first_type_implement(p_oie: OIE, p_event: Event) -> None:
    selected_2tuple = get_rand_2tuple(p_oie.I())
    p_event.set_starting_and_ending_timestamps(selected_2tuple[0], selected_2tuple[1])
