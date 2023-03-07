import logging
import os

from src.common.getPath import GetPath

class Log():

    def __init__(self, level="DEBUG"):
        # 创建日志器对象
        self.log = logging.getLogger()
        self.log.setLevel(level)

    def get_formatter(self):
        # 格式器
        console_fmt = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(Lineno)d] %(levelname)s %(message)s")
        file_fmt = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(Lineno)d] %(Levelname)s %(message)s")
        return console_fmt, file_fmt

    def console_handle(self, level="DEBUG"):
        # 控制台处理器
        console_handle = logging.StreamHandler()
        console_handle.setLevel(level)
        # 处理器添加格式器
        console_handle.setFormatter(self.get_formatter()[0])
        return console_handle

    def file_handle(self, level="DEBUG"):
        # 文件处理器
        logFilePath = os.path.join(GetPath().get_log_path(), "log.txt")
        file_handle = logging.FileHandler(filename=logFilePath, mode="a", encoding="utf-8")
        file_handle.setLevel(level)
        # 处理器添加格式器
        file_handle.setFormatter(self.get_formatter()[1])
        return file_handle

    def get_log(self):
        self.log.addHandler(self.console_handle())
        self.log.addHandler(self.file_handle())
        return self.log