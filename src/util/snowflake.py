
from snowflake import SnowflakeGenerator

gen = SnowflakeGenerator(1)

def gen_snowflake_id():
    return next(gen)

def gen_snowflake_ids(count: int):
    ids = []
    for i in range(count):
        ids.append(gen_snowflake_id())
    return ids