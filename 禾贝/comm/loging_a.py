import logging

class mig_logger():
    logger = logging.getLogger('接口日志')
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
    # logger.removeHandler(fh)
    def debug(self,msg):
        self.logger.debug(msg)
        self.rh()
    def info(self,msg):
        self.logger.info(msg)
        self.rh()
    def warning(self,msg):
        self.logger.warning(msg)
        # mig_logger.warning("断言失败了，商品创建失败")
        self.rh()
    def rh(self):
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.ch)