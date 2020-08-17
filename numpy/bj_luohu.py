import csv
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# 以dataframe格式读取前五行
csv_file = "bj_luohu.csv"
csv_data = pd.read_csv(csv_file, low_memory=False)  # 防止弹出警告
csv_df = pd.DataFrame(csv_data)
five = csv_df[:5]
print(five)
# 公司与姓名
name_company = []
name_company = csv_df[['name', 'company']]
print(name_company)
# birthday
birthdays = []
birthdays = csv_df['birthday']
print(birthdays)
old = []
for i in birthdays:
    # print(type(i))
    # print(i)
    # a = datetime.datetime.strftime('i',"%y")# %m %d %H:%M:%S
    b = datetime.datetime.strptime(i, '%Y-%m').strftime('%Y')
    old.append(b)
print(old)
# print(csv_df)
ages = []
for i in old:
    i = 2020 - int(i)
    ages.append(i)
print(ages)
csv_df['birthday_year'] = old
csv_df['age'] = ages
print(csv_df)
dalao = []
beipiao = []

dalao = csv_df[csv_df.age == 35]
beipiao = csv_df[csv_df.age == 62]
print("35岁落户北京的人有：")
print(dalao)
print("62岁落户北京的人有：")
print(beipiao)

# matplotlib模块绘制直方图
# 绘制直方图
plt.hist(x = csv_df.score, # 指定绘图数据
         bins = 20, # 指定直方图中条块的个数
         color = 'steelblue', # 指定直方图的填充色
         edgecolor = 'black' # 指定直方图的边框色
         )
# 添加标题
plt.title('落户分数（score）直方图')
# 显示图形
plt.show()
