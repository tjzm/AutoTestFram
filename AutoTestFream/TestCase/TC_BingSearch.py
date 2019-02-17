import unittest
import time
from time import sleep
from AutoTestFream.public.log import log   # 导入日志类
from AutoTestFream.public.common import TestCaseInfo,DoExcel,CommonConfig as cc
      # 导入 TestCaseInfo,DoExcel,CommonConfig 这些模块
from AutoTestFream.public.pages import bing  # 导入bing模块

# 从Excel中读取测试数据，赋予变量bing_value
bing_value = DoExcel.ReadExcel("testDemo.xlsx","Sheet1").read_excel(1,0)
bing_url = DoExcel.ReadExcel("testDemo.xlsx","Sheet1").read_excel(0,1)
'''
self.id = id
        self.name=name
        self.owner=owner
        self.result=result
        self.startime=startime
        self.endtime=endtime
        self.secondsDuration=secondsDuration
        self.errorinfo=errorinfo   '''

class Test_Bing_Search(unittest.TestCase):
    '''定义测试类，编写测试用例'''
    def setUp(self):
        # self.base_url = cc.baseUrl()  # 从cc中获取url
        self.base_url = bing_url   #  从Excel中获取url
        print(f"self.base_url = {self.base_url}")
        self.testCaseInfo = TestCaseInfo.TestCaseInfo(id=1,name="Bing Search",owner="Bela")
                             # 初始化测试用例信息
    def test_searchBing(self):
        try:
            self.startime = cc.getCurrentTime()  # 获取当前时间，作为开始时间
            # 实例化bing 中的Search类
            self.baseSearch = bing.Search()
            sleep(3)
            # 从Search类的父类BasePage中继承了open方法，打开url
            self.baseSearch.open(self.base_url)
            sleep(3)
            # 调用Search类中的Search_value（）方法，设置检索值
            self.baseSearch.Search_value(bing_value)
            sleep(4)
            #  输入日志信息
            logger = log.Runlogger("debug","TC_BingSearch").getlog()
            logger.debug(("debug:","test_searchBing 的debug 信息"))
            logger.info("test_searchBing 的 info 信息")

            # 退出
            self.baseSearch.quit()
            # t = time.time()
            # print(f"t = {t}")
            logger.debug(f"{time.time()}:退出浏览器")
        except Exception as e:
            logger = log.Runlogger("debug", "TC_BingSearch").getlog()
            logger.debug(e)
            logger.info(e)
    def tearDown(self):
        pass


#  测试
if __name__ == "__main__":
    unittest.main()

