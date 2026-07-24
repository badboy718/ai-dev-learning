import redis
from sqlalchemy import exists

r = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    decode_responses=True
)
#设置键值对
r.set('key', 'value')
#是否存在 exists
exists = r.exists('key')
print('是否存在',exists)
#设置生存时间 expire
r.expire('key', 10)
#查看剩余时长 ttl
ttl = r.ttl('key')
print('剩余',ttl)
#设置新键值对，带有生存时间
r.setex('key2',20,'value2')
#永久存在 persist
r.persist('key1')

#查找所有键
all_keys = r.keys('*')
print('所有：',all_keys)

#删除key1键
r.delete('key1')
#查看是否存在
print(r.exists('key1'))