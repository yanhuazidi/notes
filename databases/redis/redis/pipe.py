import redis, time

r = redis.Redis(host="localhost", port=6379, decode_responses=True)
r.set('wangwc','wanglaoshi')
pipe = r.pipeline(transaction=True)

pipe.set('p1','v1')
pipe.set('p2','v2')
pipe.set('p3','v3')
pipe.set('wangwc','shuaiwang')
print(r.get('wangwc'))
time.sleep(5)
pipe.execute()
print('@@@@@@@@@@@@@@@@')
print(r.get('wangwc'))