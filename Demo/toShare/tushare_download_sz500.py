#tushare lib学习
#利用 tushare 来获取 我国A股 股票代码数据

import sys,os
import tushare as ts
import pandas as pd
import time


#数据存放文件
dateStr = time.strftime("%Y-%m-%d")
rss = "/Users/yujinyu/Downloads/python/datas/"
folder = rss + dateStr
fss = rss+dateStr+"/stock_sz500.csv"
print(fss);

#入如果目录没有，则创建改目录
if not os.path.exists(folder):
    os.makedirs(folder)

if not os.path.exists(fss):
        f = open(fss, 'w')
        f.close()
        print(fss + " created.")
else:
        print(fss + " already existed.")


dat = ts.get_zz500s()
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')