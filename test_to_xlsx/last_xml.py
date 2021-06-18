# coding:utf-8
import time
import datetime
import os
a=str(os.path.abspath(os.path.join('')).split('\\')[-1])
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
directory = os.path.abspath(os.path.join(''))#.replace(a,'').replace('\\\\','\\')
#path要获取的文件路径
path = directory+"\\"
def sortfile(path):
    fl=os.listdir(path) #获取当前目录文件列表
    #时间戳进行倒序排序
    fl.sort(key=lambda fn: os.path.getmtime(path + fn) if not os.path.isdir(path + fn) else 0)
    #date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象
    dt=datetime.datetime.fromtimestamp(os.path.getmtime(path + fl[-1]))
    #dt.strftime("%Y年%m月%d日 %H时%M分%S秒" 将date对象格式化显示
    # print('最后download的文件是: ' + fl[-1])
    last_update=fl[-2]
    return last_update
if __name__ == '__main__':
    sortfile(path)