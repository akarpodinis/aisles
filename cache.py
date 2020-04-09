from os import environ

import redis

cache = redis.from_url(environ.get("REDIS_URL"), decode_responses=True)
