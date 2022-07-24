import matplotlib.pyplot as plt

from random_walk import RandomWalk

#只要程序处于活跃状态，就不断地模拟随机漫步
while True:
    #创建一个RandomWalk实例
    rw=RandomWalk()
    rw.fill_walk()

    #将所有点都绘制出来
    plt.style.use('classic')
    fig,ax=plt.subplots(figsize=(15,9))#传递参数figsize以指定生成的图形的尺寸，单位为英寸  

    #生成一个数字列表，其中包含的数与漫步包含的点的数量相同  
    point_numbers=range(rw.num_points)

    #传递参数edgecolor='none'以删除每个点周围的轮廓
    ax.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=15)

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=100)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=100)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running=input("Make another walk?(y/n): ")
    if keep_running=='n':
        break
