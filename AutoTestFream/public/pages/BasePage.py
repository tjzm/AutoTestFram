
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BasePage(object):
    '''
    BasePage类封装了所有页面的共用的方法，比如 driver/url/quit 等
    '''
    def __init__(self):
        try:
            self.driver = webdriver.Firefox()
        except Exception:
            raise NameError("Not FireFox")

    def open(self,url):
        '''
        打开 url
        :param url:
        :return:
        '''
        if url != "":
            self.driver.get(url)
            self.driver.maximize_window()
        else:
            raise ValueError("url为空或输入有误")
    def findElement(self,element):
        try:
            type = element[0]
            value = element[1]
            if type=="id" or type=="ID" or type=="Id":
                elem = self.driver.find_element_by_id(value)
            elif type=="name" or type=="NAME" or type=="Name":
                elem = self.driver.find_element_by_name(value)
            elif type=="class" or type=="CLASS" or type=="Class":
                elem = self.driver.find_element_by_class_name(value)
            elif type=="link_text" or type=="LINK_TEXT" or type=="Link_text":
                elem = self.driver.find_element_by_link_text(value)
            elif type=="xpath" or type=="XPATH" or type=="Xpath":
                elem = self.driver.find_element_by_xpath(value)
            elif type=="css" or type=="CSS" or type=="Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("未找到相应的元素属性")

        except Exception:
            raise NameError("无相应的对象"+str(element))
        return elem

    def findElements(self, element):
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_elements_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_elements_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_elements_by_class_name(value)
            elif type == "link_text" or type == "LINK_TEXT" or type == "Link_text":
                elem = self.driver.find_elements_by_link_text(value)
            elif type == "xpath" or type == "XPATH" or type == "Xpath":
                elem = self.driver.find_elements_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("未找到相应的元素属性"+str(element))

        except Exception:
            raise NameError("无相应的对象")
        return elem

    def type(self,element,Text):
        '''
        操作input box
        :param element:
        :param text:
        :return:
        '''
        print("Text = ",Text)
        element.send_keys(Text)

    def click(self,element):
        '''
        点击button
        :param element:
        :return:
        '''
        element.click()
    def enter(self,element):
        '''
        回车操作
        :param element:
        :return:
        '''
        element.send_keys(Keys.ENTER)
    def quit(self):
        self.driver.quit()
    def getAttribute(self,element,attribute):
        '''
        获取元素的属性值， get_attribute("id")
        :param element:
        :param attribute:
        :return:
        '''
        return element.get_attribute(attribute)
    def display(self,id):
        '''
        js 操作，获取界面上的隐藏元素
        :param id:
        :return:
        '''
        self.driver=webdriver.Firefox()
        js = 'document.getElementById(list[id]).style.display="block"'
        self.driver.execute_script(js)