import smtplib
from email.mime.text import MIMEText #填写文本
from email.header import Header  #标题
from email.mime.multipart import MIMEMultipart#编写文件
from readconfig import ReadConfig
from loging_a import mig_logger
from newReport import new_file
from location import result_path
#实例化html存储路径
result_path = result_path()

#实例化日志
logger = mig_logger()
# 获取配置文件
e = ReadConfig()
mail_host,mail_user,mail_pass,sender,receiver = e.email_a()

def send():
    msg = MIMEMultipart()
    msg['From'] = Header('sqb_xu@163.com')  # 编辑邮件头
    msg['To'] = Header('2422397206@qq.com')
    msg['Subject'] = Header('禾贝管理系统', 'utf-8')
        # html1 = 'D:\python3\UI自动化\\test_html\test_runner.html'
    new_file1 = new_file(result_path)
    with open(new_file1,'rb') as f:
        with_html = f.read()
        # f.close()
        msg.attach(MIMEText(with_html, 'html', 'utf-8'))  # 把正文附在邮件上
        att = MIMEText(with_html, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="test_main.html"'
        msg.attach(att)
        # smtpObj = smtplib.SMTP()

        try:
            smtpObj = smtplib.SMTP_SSL(mail_host)
            # smtpObj.connect('smtp.163.com',465)
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receiver, msg.as_string())
            smtpObj.quit()
        except:
            logger.warning('邮件发送失败')

