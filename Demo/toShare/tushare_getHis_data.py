#利用tushare 来获取历史数据
import sys,os
import tushare as ts
import pandas as pd
import matplotlib as mtl

#数据存放文件
rss = "/Users/yujinyu/Downloads/python/datas/600988"
#/Users/yujinyu/Downloads/python/datas/stock_base.csv
#print(fss)


#600988 股票代码 600988-赤峰黄金
dat = ts.get_hist_data('600988')
fss = rss + "/stock_his_data_600988_20190429.csv"
#print(dat)
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')


#指定开始时间和结束时间
#虽然可以指定时间，但是好像只能获取近一年的数据
dat = ts.get_hist_data('600988',start='2014-01-01')
fss = rss + "/stock_his_data_600988_02.csv"
#print(dat)
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')


#获取 周 k线数据
dat = ts.get_hist_data('600988',ktype='W')

#获取 月 k线数据
#dat = ts.get_hist_data('600988',ktype='M')

#获取 5分钟 k线数据
#dat = ts.get_hist_data('600988',start='2018-05-31',end='2018-06-01', ktype='5')
fss = rss + "/stock_his_data_600988_03_W.csv"
#print(dat)
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')



print('success!')


exit()