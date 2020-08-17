import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams["font.sans-serif"]=["SimHei"]
#plt.rcParams["font.family"] = 'Arial Unicode MS'	#我是mac系统，这里使用这个显示中文
#["font.sans-serif"]=["SimHei]		windows系统使用这一句
plt.figure(figsize=(10,10))
plt.subplot2grid((2,3),(0,0),colspan=2)		#两行三列的画布，列横跨2
#准备数据
x=np.linspace(0,4,100)
y=np.random.rand(100)
plt.scatter(x,y,c='c')

plt.title("散点图")

plt.subplot2grid((2,3),(0,2))	#表示第一行第二个子图

plt.title('空白区域')

plt.subplot2grid((2,3),(1,0),colspan=3)	#表示第二行第1个子图，横跨3列
x=np.linspace(0,4,100)
y1=np.sin(x)
plt.plot(x,y1,lw=2,ls='-')
plt.xlim(0,3)
plt.grid(True,ls=":",c='r')

plt.title("折线图")


plt.show()