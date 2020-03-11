#利用tushare 来获取历史数据
import sys,os
import tushare as ts
import pandas as pd
import matplotlib as mtl

#数据存放文件
rss = "/Users/yujinyu/Downloads/python/datas/600988"
#print(fss)


#600988 股票代码 600988-赤峰黄金
dat = ts.get_hist_data('600988')
fss = rss + "/stock_his_data_600988_20190429.csv"
#print(dat)
#baseData = pd.DataFrame(dat)
#baseData.to_csv(fss,encoding='gbk')
print('success!')


df_csvload = pd.read_csv('/Users/yujinyu/Downloads/python/datas/600988/stock_his_data_600988_20190429.csv',parse_dates=True,index_col=0,encoding='gb2312')
#返回前5行
print('\n 前5行--------------------------')
print(df_csvload.head(5))

#返回后5行
print('\n 后5行--------------------------')
print(df_csvload.tail(5))

print('\n columns--------------------------')
print(df_csvload.columns)

print('\n shape--------------------------')
print(df_csvload.shape)

print('\n describe--------------------------')
print(df_csvload.describe())

print('\n info--------------------------')
print(df_csvload.info())

#判断数据缺失值
print('\n isnull--------------------------')
#print(df_csvload.isnull())

#判断数据缺失值
print('\n isnull--------------------------')
print(df_csvload[df_csvload.isnull().T.any().T])

#修改数据精度
print('\n applymap--------------------------')

df_csvload2 = df_csvload.applymap(lambda x:'%0.2f'%x)
print(df_csvload2)#保留两位小数
print('\n-------------------------')
print(df_csvload2.info())

print('\n 保留2位小数-------------------------')
df_csvload3 = df_csvload.round(2)  #使用round 会保留现有的参数类型
print(df_csvload3)#保留两位小数
print(df_csvload3.info())


exit()