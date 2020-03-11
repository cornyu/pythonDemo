# 在数据可视化的过程中，图片中的文字经常被用来注释图中的一些特征。使用annotate()方法可以很方便地添加此类注释。
# 在使用annotate时，要考虑两个点的坐标：被注释的地方xy(x, y)和插入文本的地方xytext(x, y)

import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )

plt.ylim(-2, 2)
plt.show()
