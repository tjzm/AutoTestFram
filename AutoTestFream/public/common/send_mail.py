
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 发送附件需要的包
from email.mime.base import MIMEBase
from email import encoders   # 处理编码
import smtplib
import os

# 发送邮件，带html格式附件，  这个是正确的版本，且常用
def sendReport(file_new,emailName):
############ 发送邮件并添加附件 ########
    print("file_new = ",file_new)
    with open(file_new, 'rb') as f:
        mail_body = f.read()
    msg = MIMEMultipart()  # 构造附件的对象
    msg["Subject"] = Header("Bing网页测试报告", "utf-8")
    msg["From"] = "460663879@qq.com"
    msg["to"] = "460663879@qq.com;13477599022@139.com"
    msg.attach(MIMEText(mail_body,"html","utf-8"))
    # 以二进制方式打开文件
    with open(file_new, 'rb') as ff:
        # MIMEBase 表示附件的对象
        mime = MIMEBase('sms', 'html', filename=file_new)  # 或MIMEBase('text','txt',filename=attachment)
        # filename 是显示附件名称
        mime.add_header('Content-Disposition', 'attachment', filename=emailName)
        # 获取附件内容
        mime.set_payload(ff.read())
        # 编码
        encoders.encode_base64(mime)
        # 作为附件添加到邮件
        msg.attach(mime)
        print("附件添加完成")
    smtp = smtplib.SMTP("SMTP.qq.com")  # 邮件服务器
    smtp.login("460663879@qq.com", "ulbktrwlpbjmbijg")  # 账户和密码 （授权密码）
    smtp.sendmail(msg["From"], msg["to"].split(";"), msg.as_string())
    print("邮件发送完成-- YES !! ")
    smtp.quit()


#  发送带附件的邮件  ，这个发送附件是简单版（李老师讲）
def sendReportFile1(file_path):
    '''发送带附件的邮件'''
    sendfile = open(file_path,"rb").read()   # 读取路径
    msg = MIMEText(sendfile,'base64','utf-8')
    msg["Content-Type"]="application/octet-stream"
    msg["Content-Disposition"]="attachment;filename=report.html"  # 附件名
    # msg["Content-Disposition"]=f"attachment;filename={emailName}.html"  # 附件名

    msgRoot = MIMEMultipart("related")   # 附件对象
    msgRoot.attach(msg)         # 将附件对象添加到 msg

    msg["Subject"]=Header("Bing自动化测试报告",'utf-8')  # 测试报告名字
    msg["From"]="460663879@qq.com"    # 发件者
    msg["To"] = "460663879@qq.com;13477599022@139.com"

    smtp = smtplib.SMTP("SMTP.qq.com")  # 服务器地址
    smtp.set_debuglevel(1)  # 打印调试信息
    smtp.login("460663879@qq.com","ulbktrwlpbjmbijg") # 登录
    smtp.sendmail(msg["From"],msg["To"].split(";"),msg.as_string())
    smtp.quit()
    print("邮件发送完成。。。。")


#  查找测试报告目录，找到最新生成的测试报告
def newReport(testReport):
    # 返回测试报告所在目录下的所有测试报告
    lists = os.listdir(testReport)
    # 按升序排序后的测试报告列表
    lists2 = sorted(lists)     # sorted()排序函数
    file_new = os.path.join(testReport,lists2[-1])  # 最新的那个文件名（带路径）
    file_name = os.path.basename(file_new) # 纯粹的文件名
    print(file_name)
    print(file_new)
    return file_new,file_name

#   测试内容
# if __name__ == "__main__":
#     fp = "D:\study\AutoTest\EmailDemo\Report"
#     nr = newReport(fp)   #  函数有多个返回值时，一般类型是元组类型
#     print(f"type(nr[1])={type(nr[1])},nr = {nr}")
#     sendReportFile(nr[0])
