import smtplib #连接登录关闭
from email.mime.text import MIMEText #填写文本
from email.header import Header  #标题
from email.mime.multipart import MIMEMultipart#编写文件

def e_main():
    msg = MIMEMultipart()
    msg['From'] = Header('sqb_xu@163.com')  # 编辑邮件头
    msg['To'] = Header('1448690287@qq.com')
    msg['Subject'] = Header('禾贝管理系统', 'utf-8')
    # html1 = 'D:\python3\UI自动化\\test_html\test_runner.html'
    with open(r'C:\Users\Hua\jenkins\workspace\GitHub 项目\test_runner.html','rb') as f:
        with_html = f.read()
        # f.close()
        msg.attach(MIMEText(with_html, 'html', 'utf-8'))  # 把正文附在邮件上

        att = MIMEText(with_html, 'base64', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename="test_runner.html"'
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
    else:
        print('邮件发送成功')
e_main()