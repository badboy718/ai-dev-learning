import redis

r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

# 设置哈希字段
r.hset('user:1001', 'name', '李四')
r.hset('user:1001', 'age', '30')
r.hset('user:1001', 'city', '上海')

# 获取单个字段
name = r.hget('user:1001', 'name')
print(f"用户名: {name}")

# 获取所有字段
user_info = r.hgetall('user:1001')
print("用户信息:", user_info)

# 设置多个字段
r.hmset('user:1002', {
    'name': '王五',
    'age': '28',
    'city': '广州'
})

# 获取多个字段
fields = r.hmget('user:1002', ['name', 'age'])
print("指定字段:", fields)

# 获取所有字段名
field_names = r.hkeys('user:1001')
print("字段名:", field_names)

# 获取所有字段值
field_values = r.hvals('user:1001')
print("字段值:", field_values)

# 删除字段
r.hdel('user:1001', 'city')
print("删除后:", r.hgetall('user:1001'))