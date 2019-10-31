import redis

pool = redis.ConnectionPool(host="localhost", port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r2 = redis.Redis(connection_pool=pool)
r.set('wang','lixiaochao')
print(r.get('wang'))
r2.set('zhao','wangxiaochao')
print(r2.get('zhao'))

print('##################')
print(r.client_list())
print('##################')
print(r2.client_list())