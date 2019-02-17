#  控制测试用例的执行

from HTMLTestRunner import HTMLTestRunner
import unittest
import time
from AutoTestFream.config import globalconfig
from AutoTestFream.public.common import send_mail as cc

# 测试报告所在路径
report_path = globalconfig.report_path
# 测试用例路径
TestCast_path = globalconfig.TestCast_path

def AutoRun(TestCaseName):
    '''
    :param TestCaseName: 指定测试用例的名称
    :return:
    '''
    # 自动识别、加载测试用例
    dscr = unittest.defaultTestLoader.discover(TestCast_path,pattern=TestCaseName)
    now = time.strftime("%Y-%m-%d %H%M%S")  # 获取当前时间
    filename = report_path+"\\"+now+"-"+"Bing网页测试报告.html"# 拼接测试报告名称
    # emailName=now+"-"+"Bing网页测试报告.html"
    print(f"filename = {filename}")
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp,title="Bing网页自动化测试报告",description="执行情况")
    runner.run(dscr)
    fp.close()   #  一定记得要close ,不然邮件中的内容为空，且附件内容也为空

    # 发送带附件的邮件
    nr = cc.newReport(report_path)   # 函数有两个返回值
    print(f"nr[0]={nr[0]}")
    print(f"nr[1]={nr[1]}")
    cc.sendReport(nr[0],emailName=nr[1])

if __name__ == "__main__":
    AutoRun("TC_BingSearch.py")
    #AutoRun("xxx.py")     # 同时可以执行不同的用例



