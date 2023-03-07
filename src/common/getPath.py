import os

# 定义一个类，用来获取到路径
class GetPath():

    # 定义一个方法，获取到工程所在的路径
    def get_project_path(self):
        # 1.1、 找到当前文件所在的路径os.path.abspath()，表示用来获取到某个文件的绝对路径__file__表示获取到当前文件的文件名
        currentFilePath = os.path.abspath(__file__)
        # 1.2、从当前文件出发找三次上一级目录，找到工程所在的路径os.path.dirname()表示获取到某个文件的上一级目录
        project_path = os.path.dirname(os.path.dirname(os.path.dirname(currentFilePath)))
        # 获取到的工程路径返回
        return project_path

    # 定义一个方法，用来获取到测试用例所在的路径
    def get_testcase_path(self):
        # 返回获取到的测试用例所在的路径
        return os.path.join(self.get_project_path(), "src", "testcase")

    # 定义一个方法，用来获取到测试报告所在的路径
    def get_reports_path(self):
        return os.path.join(self.get_project_path(), "reports")

    # 定义一个方法，用来获取到测试日志所在的路径
    def get_log_path(self):
        return os.path.join(self.get_project_path(), "log")

    # 定义一个方法，用来获取到测试截图所在的路径
    def get_pictures_path(self):
        return os.path.join(self.get_project_path(), "pictures")

    def get_data_path(self):
        return os.path.join(self.get_project_path(), "data")

    def get_config_path(self):
        return os.path.join(self.get_project_path(), "config")
