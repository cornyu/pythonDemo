#饼图
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
sort=['Foxes', 'Cats', 'Dogs', 'Pigs']
sizes=[13, 30, 30, 37]
color=['m', 'b', 'g', 'r']
explode=(0, 0.1, 0, 0)   #分离第2类,数值表示分离远近
plt.pie(sizes,explode=explode,labels=sort,colors=color,autopct='%1.0f%%',shadow=False)  #autopct参数加百分比
plt.show()
