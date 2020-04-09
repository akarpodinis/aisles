from os import getenv

from redis import Redis

cache = Redis(host=getenv('REDIS_URL'), port=6379, db=0)
