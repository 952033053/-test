#程序主入口
import unittest,time,HTMLTestReportCN,os
from location import result_path
from e_mail import send
#实例化html存储路径
result_path = result_path()


def add_case():
    test_dir = os.path.dirname(os.path.abspath(__file__))+ r'\comm'
    suit = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    return suit

def run_case():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # filename = result_path + '/' + now + 'result.html'
    #D:\python3\接口自动化\禾贝\comm\email_html/2020-08-20 10_16_50result.html
    filename = os.path.join(result_path,now+"result.html")
    fp = open(filename,'wb')
        # pass
    #使用HTMLTestRunner打开html文件，然后执行套件，写入html文本
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title='禾贝工行商品',
                                             description='接口测试')
    #执行套件用例，unittest下Test Result控件会自动运行测试报告，然后运行测试套件，测试报告写入html文本
    add = add_case()
    runner.run(add)
    #写入完成，关闭html文本
    fp.close()
    send()
if __name__ == '__main__':
    run_case()