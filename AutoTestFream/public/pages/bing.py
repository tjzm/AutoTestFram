'''
以 bing 搜索页面为例
http://cn.bing.com/
 driver.find_element_by_xpath("//input[@id='sb_form_q']")
 driver.find_element_by_xpath("//input[@id='sb_form_go']")
'''
import time
from selenium import webdriver
from AutoTestFream.public.pages.BasePage import BasePage
import os,sys
d_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(d_path)
from AutoTestFream.public.common.DoExcel import ReadExcel

class Search(BasePage):
    searchId = ("xpath","//input[@id='sb_form_q']")
    searchBtn = ("xpath","//input[@id='sb_form_go']")
    def Search_value(self,search_value):
        '''
        在页面中输入 search_value ，搜索
        :param search_value:
        :return:
        '''
        sear = self.findElement(self.searchId)
        sear_v = self.type(sear,search_value)
        time.sleep(3)
        sear_bt = self.findElement(self.searchBtn)
        sear_cl = self.click(sear_bt)
        time.sleep(4)


# ##### 测试过程
# bs  = Search()
# # bs.open("http://cn.bing.com/")
# # bs.Search_value("柳岩")
# url = ReadExcel("testDemo.xlsx","Sheet1").read_excel(0,1)
# print(url,"  !! ",str(url))
# d_value = ReadExcel("testDemo.xlsx","Sheet1").read_excel(1,0)
# print(d_value)
# bs.open(url)
# bs.Search_value(d_value)
# time.sleep(5)
# bs.quit()