import ast
import time

import redis

if __name__ == '__main__':
    redisDb = redis.client.Redis('47.113.229.66', 6379, 1)

    aaa = redisDb.keys('*')
    for i in aaa:
        print(type(redisDb.get(i).decode('utf-8')))
