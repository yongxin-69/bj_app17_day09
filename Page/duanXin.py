from Page.pageElement import PageElement
from appium.webdriver.common.touch_action import TouchAction
from Base.base import Base

class Duan(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)
    def click_xinjian(self):
        self.click_ele(PageElement.xinjian)
    def send_lianxiren(self,text):
        self.send_ele(PageElement.lianxiren,text)
    def send_wenben(self,text):
        self.send_ele(PageElement.wenben,text)
    def click_fasong(self):
        self.click_ele(PageElement.fasong)
    def get_duanyan(self):
        result = self.find_eles(PageElement.duanyan)
        return [i.text for i in result]
    def shanchu(self):
        TouchAction(self.driver).long_press(self.find_ele(PageElement.shanchu),duration=2000).release().perform()
        self.click_ele(PageElement.shanchu1)
        self.click_ele(PageElement.queren)





















