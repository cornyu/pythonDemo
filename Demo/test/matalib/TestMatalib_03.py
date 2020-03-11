
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

#遍历显示图形
fig_ps,axes_ps = plt.subplots(2,3)
print(fig_ps)

for i in range(2):
    for j in range(3):
        axes_ps[i,j].hist(np.random.randn(500),bins=50,color='r',alpha=0.8)

plt.show()
