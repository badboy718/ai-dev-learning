import pandas as pd
orders = [
    {"category": "图书", "price": 30, "count": 4},
    {"category": "文具", "price": 5, "count": 20},
    {"category": "图书", "price": 45, "count": 2},
    {"category": "数码", "price": 300, "count": 1},
    {"category": "文具", "price": 8, "count": 10}
]

df = pd.DataFrame(orders)
print(df)
df['amount'] = df['price'] * df['count']
print(df)
df = df.groupby(['category'])['amount'].sum()
print(df)
df = df.sort_values(ascending=False)
print(df)