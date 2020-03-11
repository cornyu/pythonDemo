#对象式 绘图

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

y_value = np.random.randn(200)
x_value = np.arange(200)

ylim_min = y_value.min()-1
ylim_max = y_value.max()+1

yticks_min = y_value.min()+0.5
yticks_max = y_value.max()-0.5
ylim_setp = (yticks_max - yticks_min)/2.1
#注释(1): pyplot模块中的figure()函数创建名为fig的Figure对象。
fig = plt.figure()#注释(1)

#注释(2): 在Figure对象中创建两个Axes对象，每个Axes对象即为一个绘图区域。
ax1 = fig.add_subplot(211) # 注释(2)
ax1.plot(x_value,y_value,label=u"随机误差",ls='-',c='r',lw=1)

#注释(3):在Axes对象中增加坐标轴标签label对象、tick对象、ticklabel对象和标题title对象，也可以对坐标轴的取值范围xlim和ylim进行设定。
ax1.set_xlim(0,len(x_value))#注释(3)
ax1.set_ylim(ylim_min,ylim_max)#注释(3)
ax1.set_xticks(np.arange(0,len(x_value),20))#注释(3)
ax1.set_yticks(np.arange(yticks_min,yticks_max,ylim_setp))#注释(3)
ax1.set_xticklabels(['2015-02-01','2015-03-01','2015-04-02','2015-05-02','2015-06-02','2015-07-02','2015-08-02','2015-09-02','2015-10-02','2015-11-02'],fontsize='small')#注释(3)
ax1.set_yticklabels([u'上限预警值',u'标准值',u'下限预警值'])#注释(3)
ax1.set_title(u"对象式编程子图1")#注释(3)
ax1.set_xlabel(u"日期")#注释(3)
ax1.set_ylabel(u"数值")#注释(3)

ax2 = fig.add_subplot(212)#创建另一个Axes对象
ax2.plot(x_value,y_value,label=u"随机误差",ls='-',c='y',lw=1)
ax2.set_xlim(0,len(x_value))#调节X轴范围
ax2.set_ylim(ylim_min,ylim_max)#调节Y轴范围
ax2.set_xticks(np.arange(0,len(x_value),20))
ax2.set_yticks(np.arange(yticks_min,yticks_max,ylim_setp))
ax2.set_xticklabels(['2015-02-01','2015-03-01','2015-04-02','2015-05-02','2015-06-02','2015-07-02','2015-08-02','2015-09-02','2015-10-02','2015-11-02'],rotation=45,fontsize='small')
ax2.set_yticklabels([u'上限预警值',u'标准值',u'下限预警值'])
ax2.set_title(u"对象式编程子图2")
ax2.set_xlabel(u"日期")
ax2.set_ylabel(u"数值")

plt.show()
