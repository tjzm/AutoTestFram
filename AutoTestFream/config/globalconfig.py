
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from AutoTestFream.public.common.ReadConfigini import ReadConfigini

# 读取配置文件
# 获取 config.ini的路径
file_path = os.path.dirname(os.path.abspath(__file__))
print(file_path)

# 读取配置文件
read_config = ReadConfigini(os.path.join(file_path,"config.ini"))
print(read_config)

# 获取项目参数
project_path = read_config.getConfigValue("project","project_path")
print(project_path)

# 日志路径
log_path = os.path.join(project_path,"report","Log")
print(log_path)

# 测试用例路径
TestCast_path = os.path.join(project_path,"TestCase")
print(TestCast_path)

# 测试报告路径
report_path = os.path.join(project_path,"report","TestReport")
print(report_path)

# 测试数据路径
data_path= os.path.join(project_path,"Data","TestData")
print(data_path)





