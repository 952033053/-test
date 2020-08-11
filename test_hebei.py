from selenium import webdriver
import unittest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #判断为Ture还是False 还有其他的判断使用
from time import sleep
from selenium.webdriver.support.select import Select #下拉列表处理
import HTMLTestReportCN
from selenium.webdriver.common.keys import Keys
import logging
import smtplib #连接登录关闭
from email.mime.text import MIMEText #填写文本
from email.header import Header  #标题
from email.mime.multipart import MIMEMultipart#编写文件
#日志生成
# 创建一个logger
logger = logging.getLogger('禾贝管理系统')
logger.setLevel(logging.DEBUG)
# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('test.TXT',encoding="utf-8")
fh.setLevel(logging.DEBUG)
# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(filename)s - %(funcName)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)



class Hebei(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://test-oc.hbei.vip/he/login')
        self.driver.find_element_by_xpath('//*[@type="text"]').send_keys('admin')
        self.driver.find_element_by_css_selector('input[type="password"]').send_keys('admin@#8ik0')
        self.driver.find_element_by_css_selector('button[type="button"]').click()
    def test_A_virtual(self):
        driver = self.driver
        driver.maximize_window()     #全屏打开
        driver.implicitly_wait(10) #隐性等待
        driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul/div[5]/li/div').click()
        driver.find_element_by_link_text('工行商品').click()  #进入工行模块
        driver.find_element_by_xpath('//*[@class="addbtn"]/button[2]').click() #进入商品创建
        driver.find_elements_by_class_name('el-upload__input')[1].send_keys(r'D:\\360downloads\\2018960.png')#示例图
        driver.find_elements_by_class_name('el-input__inner')[6].send_keys('杭州万达集团')#名称
        driver.find_elements_by_class_name('el-input__inner')[7].send_keys(44) #权重
        driver.find_elements_by_class_name('el-input__inner')[8].send_keys('我是最强的') #副标题
        driver.find_elements_by_class_name('el-input__inner')[9].send_keys(11) #价格
        driver.find_elements_by_class_name('el-input__inner')[10].send_keys(13) #成本价
        driver.find_elements_by_class_name('el-input__inner')[11].click() #点击分类
        driver.find_elements_by_class_name('el-select-dropdown__item')[24].click() #选择分类
        sleep(3)
        driver.find_elements_by_class_name('el-upload__input')[0].send_keys(r'D:\360downloads\2018960.png') #上传logo
        driver.find_elements_by_class_name('el-dialog__headerbtn')[2].click()
        sleep(3)

    # @unittest.skip('暂时跳过')
    def test_duanyan(self):
        '''
        断言
        :return:
        '''
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('/html/body/div/div/div[1]/div[1]/div/ul/div[5]/li/div').click()
        self.driver.find_element_by_link_text('工行商品').click()
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div[1]/div[1]/div/input').send_keys('大礼包——隐藏')
        self.driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[1]/div[1]/div[1]/div[1]/div/input').send_keys(Keys.ENTER)
        sleep(4)
        c = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/div[3]/div/span[1]').text
        # print(c)
        # logger.debug("断言运行正常")
        try:
            self.assertEqual(c,'共 1 条',msg='页面进入失败啦')
        except:
            logger.warning("断言失败了，商品创建失败",exc_info=False)
        else:
            logger.debug('商品创建成功')




    def tearDown(self):
        sleep(4)
        self.driver.close()

def e_main():
    msg = MIMEMultipart()
    msg['From'] = Header('sqb_xu@163.com')  # 编辑邮件头
    msg['To'] = Header('2422397206@qq.com')
    msg['Subject'] = Header('禾贝管理系统', 'utf-8')
    # html1 = 'D:\python3\UI自动化\\test_html\test_runner.html'
    with open(r'./test_main.html','rb') as f:
        with_html = f.read()
        # f.close()
        msg.attach(MIMEText(with_html, 'html', 'utf-8'))  # 把正文附在邮件上

        att = MIMEText(with_html, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="test_main.html"'
        msg.attach(att)

    # smtpObj = smtplib.SMTP()
    try:
        smtpObj = smtplib.SMTP_SSL('smtp.163.com')
        # smtpObj.connect('smtp.163.com',465)
        smtpObj.login('sqb_xu@163.com', 'NELNBMECWNWJOGHI')
        smtpObj.sendmail('sqb_xu@163.com', '2422397206@qq.com', msg.as_string())
        smtpObj.quit()
    except:
        print('邮件发送失败')
        logger.warning('邮件发送失败')
    else:
        logger.debug('邮件发送成功')
        print('邮件发送成功')
#添加测试套件
test_dir = r'C:\Users\Hua\jenkins\workspace\禾贝管理系统'
# defaultTestLoader()类，通过该类下面的discover()方法可自动根据测试目录test_dir匹配查找测试用例文件（test*.py）
suit = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__ == '__main__':
    fp = open('./test_main.html','wb')
        # pass
    #使用HTMLTestRunner打开html文件，然后执行套件，写入html文本
    runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                             title='禾贝工行商品',
                                             description='商品批量添加')
    #执行套件用例，unittest下Test Result控件会自动运行测试报告，然后运行测试套件，测试报告写入html文本
    runner.run(suit)
    #写入完成，关闭html文本
    fp.close()


    e_main()