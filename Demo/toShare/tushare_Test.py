#toshare lib学习
#利用 tushare 来获取 我国A股 股票代码数据

import sys,os
import tushare as ts
import pandas as pd

df_concept = ts.get_concept_classified()#概念分类
print(df_concept.head(40))

exit()




