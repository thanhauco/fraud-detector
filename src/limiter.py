import redis
import time
r = redis.Redis()
def is_limited(ip):
    key = f'limit:{ip}'
    current = r.get(key)
    if current and int(current) > 100: return True
    r.incr(key)
    r.expire(key, 60)
    return False