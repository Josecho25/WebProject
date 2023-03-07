from selenium.webdriver.support import expected_conditions


class WebElementOperate:
    def locate_element(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element))

    def click_element(self, waitObject, element):
        waitObject.until(expected_conditions.presence_of_element_located(element)).click()

    def clear_element(self, waitObject, element):
        waitObject.until(expected_conditions.presence_of_element_located(element)).clear()

    def send_keys_to_element(self, waitObject, element, value):
        waitObject.until(expected_conditions.presence_of_element_located(element)).send_keys(value)

    def get_element_text(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).text

    def get_element_tag_name(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).tag_name

    # 获取元素的属性值
    def get_element_attribute(self, waitObject, element, attribute):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).get_attribute(attribute)

    def get_into_iframe(self, waitObject, iframe):
        waitObject.until(expected_conditions.frame_to_be_available_and_switch_to_it(iframe))

    def switch_to_parent_or_default_iframe(self, driver_browser, chooseIframe='default'):
        if chooseIframe == 'parent':
            driver_browser.switch_to.parent_frame()
        else:
            driver_browser.switch_to.default_content()

    # 检测该元素是否对用户可见，返回的是布尔值
    def detect_element_is_displayed(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).is_displayed()

    # 检测该元素是否可用。如果标签中有一个disabled属性的值是disabled，则该元素就不可用，返回的是布尔值
    def detect_element_is_enabled(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).is_enabled()

    # 检测该元素是否被选中，一般检测的是复选框或者单选框是否被选中，返回的是布尔值
    def detect_element_is_selected(self, waitObject, element):
        return waitObject.until(expected_conditions.presence_of_element_located(element)).is_selected()
