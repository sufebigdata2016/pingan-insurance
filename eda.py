import pandas as pd

train_path = "PINGAN-2018-train_demo.csv"
train_data = pd.read_csv(train_path)
"""
  用户id：用户唯一标志。

  unix时间戳：从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数，不考虑闰秒。

  行程id：用户行程唯一标志。

  经度：用户行程目前所在经度。

  纬度：用户行程目前所在维度。

  方向(角度)：用户行程目前对应方向，正北为0，顺时针方向计算角度（如正东为90、正南为180），负值代表此时方向不可判断。

  海拔(m)：用户行程目前所处的海拔高度。

  速度(km/h)：用户行程目前的速度。

  电话状态：用户行程目前的通话状态。（0,未知 1,呼出 2,呼入 3,连通 4,断连）

  客户赔付率：客户赔付情况，为本次建模的目标Y值。（test中不含此字段）
"""
train_data.head()
train_data.shape  # (69306, 10)
train_data[train_data.Y > 0].shape  # (8529, 10)
train_data.TERMINALNO.unique()  # 1-100
train_data.describe()
train_data.dtypes

# 每个用户只有一种赔付率
train_data.Y.unique()
train_data.Y.mean()

# 画三维图

def a():
    return 

if __name__ == "__main__":

    print(1)