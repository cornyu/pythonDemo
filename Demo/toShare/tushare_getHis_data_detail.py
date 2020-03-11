#利用tushare 来获取历史数据
import sys,os
import tushare as ts
import pandas as pd
import matplotlib as mtl
import time

#基础数据
startDate = '2018-09-21'
endDate = '2018-09-21'
baseCode = '600988'  #赤峰黄金


#数据存放文件
dateStr = time.strftime("%Y-%m-%d")
rss = "/Users/yujinyu/Downloads/python/datas/"
folder = rss + dateStr +"/"
fss = folder+"sz500.csv"
print(fss);

#入如果目录没有，则创建改目录
if not os.path.exists(folder):
    os.makedirs(folder)
else:
    print(folder + " already existed.")

if not os.path.exists(fss):
        f = open(fss, 'w')
        f.close()
        print(fss + " created.")
else:
        print(fss + " already existed.")


#dat 类型：pandas.core.frame.DataFrame
dat = ts.get_hist_data(baseCode,start=startDate,end=endDate)
baseData = pd.DataFrame(dat)
baseData['code'] = baseCode
print(baseData)
print("--------------")



# print("600004")
# dat600004 = ts.get_hist_data('600004',start='2018-09-20',end='2018-09-22')
# print(dat600004)
#
# print("dat")
# dat = dat.append(dat600004)
# print(dat)


#读取上证500 所有的公司代码
sz500FilePath = "/Users/yujinyu/Downloads/python/datas/2018-09-24/stock_sz500.csv"
train_data = pd.read_csv(sz500FilePath,encoding='gbk')
#print(train_data)
codes = train_data.pop('code')
#print(codes)
print("code个数：")
print(len(codes))
nums = len(codes)


for num in range(0, 500):  # 迭代 0 到 nums 之间的数字
    print("-----start")
    code = str(codes[num])
    codeStr = str(codes[num])
    #print(len(code))
    codeLen = len(code)
    #print(type(codeLen))
    if codeLen < 6:
        addSum = 6-codeLen
        print("需要补充0:"+codeStr)
        #print(addSum)
        count = 0
        while(count < addSum):
            codeStr = "0"+codeStr
            count = count + 1


    #print(codeStr)
    print("+++++end")
    data = ts.get_hist_data(codeStr, start=startDate, end=endDate)
    result = pd.DataFrame(data)
    print(result)
    if result.empty:
        print("没找到code:" + codeStr +" 的数据")
    else:
        result['code'] = codeStr
        baseData = baseData.append(result)

    #print(baseData)



print(len(baseData))
#baseData = pd.DataFrame(baseData)
baseData.to_csv(fss,encoding='gbk')


exit(0)






