import logging
import os,time
from AutoTestFream.config import globalconfig
log_path = globalconfig.log_path
print(f"log_path={log_path}")

class Runlogger(object):
    def __init__(self,level,logger):
        '''
        :param level: 指定日志级别
        :param logger:将日志存放的目录
        '''
        if level == "info":
            setloglevel = logging.INFO
        elif level == "debug":
            setloglevel = logging.DEBUG
        elif level == "warning":
            setloglevel = logging.WARNING
        elif level == "error":
            setloglevel = logging.ERROR
        # 设置日志文件的名称
        self.LogFileName = os.path.join(log_path,"{0}.log".format(time.strftime("%Y-%m-%d")))

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(setloglevel)

        fh = logging.FileHandler(self.LogFileName)
        fh.setLevel(setloglevel)

        ch = logging.StreamHandler()
        ch.setLevel(setloglevel)

        # 设置日志格式
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger

# #  测试内容
# rl = Runlogger("debug","fox").getlog()
# rl.debug("debug日志信息")
# rl.info("info日志信息")