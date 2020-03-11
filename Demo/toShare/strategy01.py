#策略1： 获取每天涨停的股票，统计第二天继续涨的股票，统计这样的概率；如果概率大，那么可以每天统计下涨停的股票，并在第二天买入，第三天卖出来盈利；


import sys,os
import tushare as ts
import pandas as pd

import pandas_datareader.data as web
import datetime


df_stockload = web.DataReader("000001.SS", "yahoo", datetime.datetime(2017,1,1), datetime.date.today())
