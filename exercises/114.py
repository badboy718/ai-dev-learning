import re

# 定义一个函数,用于处理数据
def show(data):
    if data:
        print('匹配成功:', data.group())
    else:
        print('匹配失败!')


# | :   匹配左右任意一个表达式    或者
# ():   小括号中内容为一组,默认产生从1开始的编号
# 需求.匹配出163,qq,sina的邮箱地址，且@符号之前有4到20位，举例: hello@163.com
result = re.match('([a-zA-Z0-9_]{4,20})@(163|qq|sina)\.com', 'binzi@qq.com')
show(result)
print(result.group(0)) # 0拿的是所有匹配成功的数据
print(result.group(1)) # 根据分组编号1,拿到对应的分组
print(result.group(2)) # 根据分组编号2,拿到对应的分组

# \n:   根据分组编号n引用对应的分组
result = re.match('<([a-zA-Z1-6]+)>.*</\\1>', '<html>标签内容</html>')
show(result)

# (?P<name>) : 给分组起别名name
# (?P=name) :  根据分组名name引用对应的分组
result = re.match('<(?P<name1>[a-zA-Z1-6]+)>.*</(?P=name1)>', '<html>标签内容</html>')
show(result)