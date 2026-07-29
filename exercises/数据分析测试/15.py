import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False

sales = [
    {"month": "1月", "category": "图书", "amount": 1200},
    {"month": "1月", "category": "文具", "amount": 800},
    {"month": "2月", "category": "图书", "amount": 1500},
    {"month": "2月", "category": "文具", "amount": 950},
    {"month": "3月", "category": "图书", "amount": 1800},
    {"month": "3月", "category": "文具", "amount": 1100},
]
df = pd.DataFrame(sales)


month_total = df.groupby("month")["amount"].sum()
print(month_total)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(month_total.index, month_total.values, marker='o', color='#2E86AB')
plt.title("月度整体销售趋势")
plt.xlabel("月份")
plt.ylabel("总销售额")


cate_total = df.groupby("category")["amount"].sum()
print(cate_total)

plt.subplot(1, 2, 2)
plt.bar(cate_total.index, cate_total.values, color='#A23B72')
plt.title("商品分类总销售额对比")
plt.xlabel("商品分类")
plt.ylabel("总销售额")


plt.tight_layout()

plt.show()
