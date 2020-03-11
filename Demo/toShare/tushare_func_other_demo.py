#利用tushare 来获取股票数据

import sys,os
import tushare as ts
import pandas as pd
import matplotlib as mtl

#数据存放文件
rss = "/Users/yujinyu/Downloads/python/datas"
#/Users/yujinyu/Downloads/python/datas/stock_base.csv
#print(fss)


#600988 股票代码 600988-赤峰黄金
#获取历史分笔数据
dat = ts.get_tick_data('600988',date='2018-06-01')
fss = rss + "/stock_tick_data_600988_01.csv"
#print(dat)
baseData = pd.DataFrame(dat)
#baseData.to_csv(fss,encoding='gbk')
print(dat.head(10))

#获取 大盘指数行情
print('\n大盘指数行情')
dat = ts.get_index()
fss = rss + "/stock_index_data_大盘指数行情_01_.csv"
print(dat)
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')


#获取 大单交易数据
# 接口好像获取不到数据

print('\n大单交易数据')
dat = ts.get_sina_dd('600848',date='2018-04-01',vol='400')
fss = rss + "/stock_sina_dd_data_600848_01_.csv"
print(dat)
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')




exit()