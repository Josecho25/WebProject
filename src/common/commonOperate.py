import os
import time

from selenium.webdriver.support.select import Select

from src.common.getPath import GetPath
from src.common.webElementOperate import WebElementOperate


class GeneralOperate:
    def get_screenshot(self, driverBrowser, testCaseName):
        screenshotName = self.system_time_stamp() + '_' + testCaseName + '.png'
        picturesPath = os.path.join(GetPath().get_picture_path(), screenshotName)
        driverBrowser.get_screenshot_as_file(picturesPath)

    # 定义一个函数，用来把系统的当前时间转换成年月日时分秒的格式
    def system_time_stamp(self):
        return time.strftime("%Y%m%d%H%M%S", time.localtime())

class WindowOperate:
    def open_url(self, driverBrowser, url):
        return driverBrowser.get(url)

    def max_window(self, driverBrowser):
        return driverBrowser.maximize_window()

    def min_window(self, driverBrowser):
        return driverBrowser.minimize_window()

    def set_window_size(self, driverBrowser, width, height):
        return driverBrowser.set_window_size(width, height)

    def back_window(self, driverBrowser):
        return driverBrowser.back()

    def forward_window(self, driverBrowser):
        return driverBrowser.forward()

    def refresh_window(self, driverBrowser):
        return driverBrowser.refresh()

    def close_window(self, driverBrowser):
        return driverBrowser.close()

    def quit_browser(self, driverBrowser):
        return driverBrowser.quit()

    def get_window_title(self, driverBrowser):
        return driverBrowser.title

    def get_current_url(self, driverBrowser):
        return driverBrowser.current_url

# select标签的下拉框的选择,通过Select类
class SelectTagChoose:
    # 通过选项元素（即option标签）的value属性的值来选择下拉框中的选项
    def select_by_value(self, waitObject, element, value):
        Select(WebElementOperate().locate_element(waitObject, element)).select_by_value(value)

    # 通过选项元素（即option标签）的可视文本内容来选择下拉框中的选项
    def select_by_text(self, waitObject, element, text):
        Select(WebElementOperate().locate_element(waitObject, element)).select_by_visible_text(text)

    # 通过选项元素（即 option标签）对应的索引来选择下拉框中的选项, 索引是从0开始计算
    def select_by_index(self, waitObject, element, index):
        Select(WebElementOperate().locate_element(waitObject, element)).select_by_index(index)

# 弹窗操作
class AlertOperate:
    def click_alert_accept(self, driverBrowser):
        driverBrowser.switch_to.alert.accept()

    def click_alert_cancel(self, driverBrowser):
        driverBrowser.switch_to.alert.dismiss()

    def send_keys_to_alert(self, driverBrowser, value):
        driverBrowser.switch_to.alert.send_keys(value)

    def get_alert_text(self, driverBrowser):
        return driverBrowser.switch_to.alert.text

# 多窗口切换
class SwitchWindow:
    def switch_window(self, driverBrowser, targetWindowTitle):
        # currentHandle = driverBrowser.current_window_handle
        # 获取所有窗口句柄，列表
        handles = driverBrowser.window_handles
        for handle in handles:
            # 进行切换
            driverBrowser.switch_to.window(handle)
            # 然后进行判断
            if driverBrowser.title == targetWindowTitle:
                break
