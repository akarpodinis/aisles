from os import environ

import redis

cache = redis.from_url(environ.get("REDIS_URL"))
