# 修饰符: 正则表达式可以包含一些可选标志修饰符来控制匹配的模式
#
# 常见的修饰符
#
# re.I : 设置当前匹配不区分大小写
#
# re.S : 设置.真正匹配到任意字符包含\n

# 导包
import re

# 演示不区分大小写的匹配:re.I
# 注意: 验证码必须绝对匹配,可以使用^和$配合起到限制作用
data = re.findall('^a8D9$', 'A8d9', re.I)
print(data)  # ['A8d9']

# 演示.真正匹配到任意字符包含\n: re.S
print('------------------------')
my_str = '123\n456\n789'
print(my_str)
print('------------------------')
data = re.match('.{7}', my_str)
print(data)  # None  因为.不能匹配到\n
print('------------------------')
data = re.match('.{7}', my_str, re.S)
print(data.group())  # 123\n456  因为re.S让.匹配到了\n