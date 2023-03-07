import unittest

from parameterized import parameterized
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from src.common.logOperate import Log


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driverBrowser = webdriver.Chrome()
        self.waitObject = WebDriverWait(self.driverBrowser, 10)
        self.logger = Log().get_log()

    @classmethod
    def setUpClass(cls):   # 这个方法在类执行之前执行
        pass

    @parameterized.expand()
    def test_case(self):
        try:
            pass
            self.logger.critical("start")
            # self.assertEqual(expectResult, actualResult)
        except:
            pass
            raise

    def tearDown(self):
        self.driverBrowser.quit()

    @classmethod
    def tearDownClass(cls):   # 这个方法在类执行之后执行
        pass