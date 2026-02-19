from typing import List
from snowflake import SnowflakeGenerator
from sqlalchemy import BigInteger

gen = SnowflakeGenerator(1)

def gen_snowflake_id() -> BigInteger | None:
    return next(gen)

def gen_snowflake_ids(count: int):
    ids: List[BigInteger | None] = []
    for i in range(count):
        ids.append(gen_snowflake_id())
    return ids