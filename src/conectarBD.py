import redis

def conectar():
    myRedis = redis.Redis(
    host='redis-10018.c299.asia-northeast1-1.gce.cloud.redislabs.com',
    port='10018',
    password='password'
    )
    return myRedis

    
