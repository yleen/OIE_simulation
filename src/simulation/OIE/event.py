from sqlalchemy import BigInteger

from util.snowflake import gen_snowflake_id


class Event:
    def __init__(self, p_name: str) -> None:
        self._name = p_name
        self._id = gen_snowflake_id()
        self._event_star_id = None

    def __str__(self) -> str:
        format_str: str = f"{self._name}(id:{self._id})"
        return format_str

    def get_id(self) -> BigInteger:
        return self._id

    def set_bijective_event_star_id(self, p_event_star_id: BigInteger):
        self._event_star_id = p_event_star_id

    def get_bijective_event_star_id(self):
        return self._event_star_id
