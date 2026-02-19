from sqlalchemy import BigInteger

from simulation.base.structure import LiZhongYuanSet
from simulation.oie.event import Event
from util.snowflake import gen_snowflake_id


class EventStar:
    def __init__(self, p_name: str) -> None:
        self._name: str = p_name
        self._id: BigInteger = gen_snowflake_id()
        self._mapped_event_id: BigInteger | None = None

    def __str__(self) -> str:
        format_str: str = f"{self._name}(id:{self._id})"
        return format_str

    def get_bijective_event_id(self) -> BigInteger:
        return self._mapped_event_id

    def set_bijective_event_id(self, p_event_id: BigInteger) -> None:
        self._mapped_event_id = p_event_id


class EventStarS(LiZhongYuanSet):
    pass


def set_bijection(p_event: Event, p_event_star: EventStar) -> None:
    p_event.set_bijective_event_star_id(p_event_star.get_bijective_event_id())
    p_event_star.set_bijective_event_id(p_event.get_bijective_event_star_id())
