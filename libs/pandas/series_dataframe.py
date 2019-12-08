import pandas as pd ;
import numpy as np

rooms = pd.Series([2,3,4]);
value = pd.Series([40000,50000,60000]);
house = pd.DataFrame({'room':rooms,'value':value});

print(type(house))
print(type(house['room']))
print(house.describe())
print(house.head())

# visit data
print(house[0:2])
print(house['value'])

# manipulate
print(house/1000)
value.apply(lambda val: val > 100)

# index
house.reindex([2, 0, 1])
## 如果您的 reindex 输入数组包含不存在的索引值，则添加新行并填充 NaN 值：
house.reindex(np.random.permutation(house.index))
