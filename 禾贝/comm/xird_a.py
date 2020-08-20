import xlrd
import os
report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + r'\接口数据.xlsx'
# print(report_path)
class xlrd_rb():
    '''
    获取url，请求方式，参数行数和对应信息
    '''
    list_api = []
    # def __init__(self,path):
    #     self.path = path

    def line(self,path):
        data = xlrd.open_workbook(path)
        sheet = data.sheet_by_index(0)
        line = sheet.nrows
        for i in range(1,line):
            a = sheet.row_values(i)
            self.list_api.append({'row':i,
                                  'url':a[1],
                                  'method':a[2],
                                   'data1':eval(a[3]),
                                    'code':a[4]})
        return self.list_api


if __name__ == '__main__':
    a = xlrd_rb()
    print(a.line(report_path))



