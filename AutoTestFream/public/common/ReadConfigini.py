import configparser
import os
import codecs

class ReadConfigini(object):
    '''
    实例化。。。。
    '''
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    # 读取操作
    def getConfigValue(self,section,option):
        value = self.cf.get(section,option)
        return value


'''测试 ReadConfigini 类'''
# file_path = os.path.dirname(os.path.abspath(__file__))
# print(f"file_path = {file_path}")
# rc = ReadConfigini(os.path.join(file_path,"test.ini"))
# c = rc.getConfigValue("cmd","file_name")
# r = rc.getConfigValue("project","file_path")
# print(c)
# print(r)
