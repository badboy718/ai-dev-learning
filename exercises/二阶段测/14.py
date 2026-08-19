import pandas as pd
import matplotlib.pyplot as plt
# 解决中文乱码警告
plt.rcParams["font.family"] = ["SimHei"]   # 设置黑体
plt.rcParams["axes.unicode_minus"] = False # 解决负号显示异常

orders = [
    {"category": "图书", "amount": 120},
    {"category": "文具", "amount": 80},
    {"category": "图书", "amount": 200},
    {"category": "数码", "amount": 500},
    {"category": "文具", "amount": 150}
]
df = pd.DataFrame(orders)
print('df\n',df)
df_category = df.groupby("category")["amount"].sum()
print('按category分组，统计销售总额\n',df_category)
result = df_category[df_category > 200]
print('筛选总额大于200的分类\n',result)

df_category.plot(kind="bar")
plt.xlabel("商品分类")
plt.ylabel("销售总额")
plt.title("各分类销售总额柱状图")
plt.show()