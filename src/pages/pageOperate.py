from selenium.webdriver.common.by import By



class Page:
    # CSS SELECTOR: #id属性 .class属性 标签名 [属性名=“属性值”] >子元素 空格直系后代 +相邻兄弟 ~后续兄弟 :nth-child(n)伪类
    CssSelectorLocation = (By.CSS_SELECTOR, 'CSS selector')
    # XPATH: /绝对路径 //相对路径 ..父节点 //tag[n]任意节点下第n个tag (//tag)[n]所有tag中的第n个
    # //tag[@属性名=”属性值”] //tag[contains(@属性名,“部分属性值”)] and *替代tag或者属性
    # //tag[starts-with(@属性名,“属性值的开头部分”)] //tag[ends-with(@属性名,“属性值的结尾部分”)]
    # //tag[text()=”全部的文本内容”] //tag[contains(text(),“部分的文本内容”)]
    # //tag[starts-with(text(),“文本内容的开头部分”)] //tag[ends-with(text(),“文本内容的结尾部分”)]
    # parent:: child:: ancestor:: descendant:: preceding::索引开始是1 preceding-sibling::索引开始是1 following:: following-sibling::
    XpathLocation = (By.XPATH, 'XPATH')
    # 通过id属性值
    IdLocation = (By.ID, 'ID')
    # 通过class属性值
    ClassLocation = (By.ID, 'class name')

    def page_operate(self):
        pass