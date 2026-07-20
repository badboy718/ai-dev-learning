import redis

# 创建 Redis 连接对象
r = redis.Redis(
    host='localhost',  # Redis 服务器地址
    port=6379,         # Redis 服务器端口
    db=0,              # 数据库编号，默认0
    password=None,     # 密码，如果没有设置密码则为None
    decode_responses=True  # 自动解码，返回字符串而不是字节
)

# 测试连接
try:
    response = r.ping()
    print("Redis 连接成功:", response)
except redis.ConnectionError as e:
    print("Redis 连接失败:", e)