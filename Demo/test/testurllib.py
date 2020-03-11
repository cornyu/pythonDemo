import urllib.request
f = urllib.request.urlopen('https://www.baidu.com/')
firstLine = f.readline()
print(firstLine)