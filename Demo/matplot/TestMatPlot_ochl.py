#饼图
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

import numpy as np

import matplotlib.pyplot as plt

import matplotlib.dates as mdates

import mpl_finance as mpf
# 替换 #import matplotlib.finance as mpf

import pandas as pd

import pandas_datareader.data as web

import datetime

import tushare as ts

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

df_stockload = web.DataReader("600797.SS", "yahoo", datetime.datetime(2018, 1, 1), datetime.date.today())

fig = plt.figure(figsize=(8, 6), dpi=100, facecolor="white")  # 创建fig对象

fig.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)

graph_KAV = fig.add_subplot(1, 1, 1)  # 创建子图

mpf.candlestick2_ochl(graph_KAV, df_stockload.Open, df_stockload.Close, df_stockload.High, df_stockload.Low, width=0.5,
                      colorup='r', colordown='g')  # 绘制K线走势

graph_KAV.set_title(u"600797 浙大网新-日K线")

graph_KAV.set_xlabel(u"日期")

graph_KAV.set_ylabel(u"价格")

graph_KAV.set_xlim(0, len(df_stockload.index))  # 设置一下x轴的范围

graph_KAV.set_xticks(range(0, len(df_stockload.index), 15))  # X轴刻度设定，每15天标一个日期

graph_KAV.grid(True, color='k')

graph_KAV.set_xticklabels(
    [df_stockload.index.strftime('%Y-%m-%d')[index] for index in graph_KAV.get_xticks()])  # 标签设置为日期

# X轴每个ticker标签都向右倾斜45度

for label in graph_KAV.xaxis.get_ticklabels():
    label.set_rotation(45)

    label.set_fontsize(10)  # 设置标签字号

plt.show()