import unittest

from BeautifulReport import BeautifulReport

from src.common.commonOperate import GeneralOperate
from src.common.getPath import GetPath


class RunCase:
    def run_case(self):
        testCasePath = GetPath().get_testcase_path()
        suites = unittest.defaultTestLoader.discover(start_dir=testCasePath, pattern='*case.py')
        reportsPath = GetPath().get_reports_path()
        system_time = GeneralOperate().system_time_stamp()
        reportsName = system_time + '_WebProject' + '.html'
        BeautifulReport(suites).report(description='description', filename=reportsName, report_dir=reportsPath)

if __name__ == '__main__':
    RunCase().run_case()
    print('hello')
    print('hello2')