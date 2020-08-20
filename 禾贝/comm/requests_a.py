#接口封装，重构


import requests
import json
from loging_a import mig_logger
logger = mig_logger()
class requests_main():
    def requests_get(self,url,data):
            res = requests.get(url,data).json()
            return res
    def requests_post(self,url,data):
            res = requests.post(url,data).json()
            return res
    def run(self,method,url,data):
        res = None
        if method == 'get':
            res = self.requests_get(url,data)
        elif method == 'post':
            res = self.requests_post(url,data)
        else:
            logger.warning('请求方式填写错误')
        return res
if __name__== '__main__':
    a = requests_main()
    b = a.run('get','http://apis.juhe.cn/sxpd/query',{'men':'蛇','women':'羊',
' key':'f45a9eb00cf5af819d561a9a9c46eb15'},)
    print(b)
