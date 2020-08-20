import configparser
import os

class ReadConfig():
    """读取.ini配置文件"""

    def __init__(self):

        # 获取配置文件路径
        config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\config.ini"
        # print(config_path)
        # 实例化configparse对象
        self.conf = configparser.ConfigParser()
        # 调用读取方法读取config.ini
        self.conf.read(config_path, encoding="utf-8-sig")

    def config(self,a,b):
    #     """获取邮件配置项内容"""
        mail_host = self.conf.get(a, b)

        return mail_host
    def email_a(self):
        mail_host = self.conf.get('EMAIL', 'mail_host')
        mail_user = self.conf.get('EMAIL', 'mail_user')
        mail_pass = self.conf.get('EMAIL', 'mail_pass')
        sender = self.conf.get('EMAIL', 'sender')
        receiver = self.conf.get('EMAIL', 'receiver')
        return mail_host,mail_user,mail_pass,sender,receiver


if __name__ == '__main__':
    a = ReadConfig()
    # a.get_email()

