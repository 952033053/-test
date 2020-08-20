import unittest
from xird_a import xlrd_rb
from ddt import ddt, unpack, data
from openpyxl_a import open_wb
import os
import json
from requests_a import requests_main
from loging_a import mig_logger
from readconfig import ReadConfig
# report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\接口数据.xlsx'
#获取配置文件
c = ReadConfig()
report_path = c.config('PATH','path')

#实例化日志类
logger = mig_logger()

#实例化读取excel，获取接口数据
rb = xlrd_rb()
line =rb.line(report_path)

#实例化测试报告写入excel
r = requests_main()

#实例化requests发送请求
wb = open_wb(report_path)
@ddt
class MyTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        '''可以用来准备测试环境的前置条件'''
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        '''可以用来完成测试完成后的数据清洗工作'''
        pass

    def setUp(self) -> None:
        '''
        每个测试用例的前置条件
        每个testcase运行前都会执行一遍
        '''
        pass

    def tearDown(self) -> None:
        '''
        每个测试用例完成的数据清洗
        每个testcase结束后都会执行一次
        '''
        pass

    @data(*line)
    @unpack
    def test_api(self,row,url,method,data1,code):
        res = r.run(method,url,data1)
        # res = json.dumps(res,indent=2,ensure_ascii=False)
        # res = json.loads(res)
        code1 = code
        row1 = row
        if code1 == res['reason']:
            wb.write(row1,code1,'通过')
        else:
            logger.warning('接口断言错啦')


if __name__ == '__main__':
    unittest.main()