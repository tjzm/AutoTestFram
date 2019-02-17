#  通用的配置文件

from datetime import datetime

def baseUrl():
    return "http://cn.bing.com"

def getCurrentTime():
    '''获取当前时间'''
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)

def timeDiff(startime,endtime):
    '''执行时间'''
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strftime(endtime,format) - datetime.strftime(startime,format)

searchContent = "Bela"
