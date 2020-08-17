import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

csv_file = "seeds_dataset.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data)
print(csv_df)
#csv_df.rename = (column = {'1 面积A',"2 周长P","3 紧凑度C = 4 pi A / P ^ 2","4 籽粒长度","5 籽粒宽度","6 不对称系数","7 核槽的长度"})
csv_df.loc['0']=["1 面积A","2 周长P","3 紧凑度C = 4 pi A / P ^ 2","4 籽粒长度","5 籽粒宽度","6 不对称系数","7 核槽的长度"]
print(csv_df.shape)
print(csv_df)
my_matrix = np.loadtxt(open("seeds_dataset.csv", "rb"), delimiter = ",")
print(my_matrix)
print(my_matrix.shape)