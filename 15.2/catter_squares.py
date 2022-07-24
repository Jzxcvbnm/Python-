import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']#显示中文标签

x_values=range(1,1001)
y_values=[x**2 for x in x_values]

fig,ax=plt.subplots()

#将参数c设置成一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=5)

#ax.scatter(x_values,y_values,c=(0,0.5,0.5),s=5)scatter()使用参数s设置绘制图形时使用的点的尺寸,参数c设置为一个元组，其中包含三个0~1的小数值，分别表示红色、绿色和蓝色的分量.值越接近0，指定颜色越深，否则反之.

#设置图表标题并给坐标轴加上标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方",fontsize=14)

#标记刻度标记的大小
ax.tick_params(axis='both',which='major',labelsize=10)

#打开Matplotlib查看器并显示绘制的图表
plt.show()
#plt.savefig('squares_plot.png',bbox_inches='tight')让程序自动将图表保存在文件中,第一个实参指定要以什么文件名保存图表，这个文件将存储到scatter_squares.py的目录,第二个实参指定将图标多余的空白区域裁剪掉