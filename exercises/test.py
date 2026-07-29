import pandas as pd
data = [
    ['stu1',60],
    ['stu2',70],
    ['stu3',80],
    ['stu4',90],
    ['stu5',100]
]
df = pd.DataFrame(data,columns=['stu_id','score'],
                  index=['row1','row2','row3','row4','row5'])
print(df)
print("=" * 20)
print(df['score'] > 80)
print("=" * 20)
print(df.loc[df['score'] > 80])
print("=" * 20)