
import xlrd
import os
from AutoTestFream.config import globalconfig
data_path = globalconfig.data_path

class ReadExcel(object):
    '''
    '''
    def __init__(self,filename,sheetname):
        d_path = os.path.join(data_path,filename)
        print(f"d_path = {d_path}")
        self.workbook = xlrd.open_workbook(d_path)
        # self.workbook = xlrd.open_workbook(filename)
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    def read_excel(self,rownum,colnum):
        ''''''
        # value = self.sheetName.cell(rownum,colnum)  # 不加 .value返回的是 text:'ss' 这样的
        value = self.sheetName.cell(rownum,colnum).value    # 加 .value 返回的才是单元格内的值（如:ss,就不会是text:'ss'）
        return value

 # 测试
v = ReadExcel("testDemo.xlsx","Sheet1").read_excel(0,0)
v1 = ReadExcel("testDemo.xlsx","Sheet1").read_excel(0,1)
print(v)
print(v1)