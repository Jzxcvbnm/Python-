import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']#显示中文标签

squares=[1,4,9,16,25]
fig,ax=plt.subplots()#变量fig表示整张图片，变量ax表示图片中的各个图表
ax.plot(squares,linewidth=1)#方法plot根据给定数据以有意义的方式绘制图表

#设置图表标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)

#标记刻度标记的大小
ax.tick_params(axis='both',labelsize=14)

plt.show()#打开Matplotlib查看器并显示绘制的图表
