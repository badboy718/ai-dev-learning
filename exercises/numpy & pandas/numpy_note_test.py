import numpy as np
arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(arr)
print('总和',np.sum(arr))
print('每列总和',np.sum(arr,axis=0))
print('每行总和',np.sum(arr,axis=1))

print('平均值',np.mean(arr))
print('标准差',np.std(arr))
print('方差',np.var(arr))

print('最小值',np.min(arr))
print('最大值',np.max(arr))
print('最小值索引',np.argmin(arr))
print('最大值索引',np.argmax(arr))