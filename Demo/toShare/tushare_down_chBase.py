#tushare lib学习
#利用 tushare 来获取 我国A股 股票代码数据

import sys,os
import tushare as ts
import pandas as pd

#数据存放文件
rss = "/Users/yujinyu/Downloads/python/datas"
fss = rss + "/stock_base.csv"
#/Users/yujinyu/Downloads/python/datas/stock_base.csv
#print(fss)

#1.获取沪深上市公司基本情况
dat = ts.get_stock_basics()
#print(type(dat))  #<class 'pandas.core.frame.DataFrame'>

baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')

#2.获取部分列的数据
c20 = ['code', 'name', 'industry', 'area']
d20 = baseData.loc[:, c20]
d20['code'] = d20.index;
fss = rss + "/stock_code.csv";print(fss);
d20.to_csv(fss,encoding='gbk')

#3.上证50成分股 ，上证规模大，流动性好的50只股票
# 上证50 ，指数代码 000016
fss = rss + "/stock_sz50.csv";print(fss);
dat = ts.get_sz50s();
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')

#4.沪深300
fss = rss +"/stock_hs300.csv";
print(fss);
dat = ts.get_hs300s();
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')

#5.上证500
fss = rss+"/stock_sz500.csv";
print(fss);
dat = ts.get_zz500s()
baseData = pd.DataFrame(dat)
baseData.to_csv(fss,encoding='gbk')

exit()




