from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self,driver):
        self.driver = driver
    def find_ele(self,loc,timeout=5,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))
    def find_eles(self,loc,timeout=5,poll_frequency=1):
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_elements(*loc))
    def click_ele(self,loc,timeout=5,poll_frequency=1):
        self.find_ele(loc,timeout,poll_frequency).click()
    def send_ele(self,loc,text,timeout=5,poll_frequency=1):
        self.find_ele(loc,timeout,poll_frequency).clear()
        self.find_ele(loc, timeout, poll_frequency).send_keys(text)

if __name__ == '__main__':
    from appium import webdriver
    import time
    # 创建驱动对象
    d = {}
    d["platformName"]= "Android"
    d["platformVersion"]= "5.1"
    d["deviceName"]= "模拟器"
    d["appPackage"]= "com.android.mms"
    d["appActivity"]=".ui.ConversationList"
    d["resetKeyboard"]=True
    d["unicodeKeyboard"]=True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
    base = Base(driver)
    base.click_ele((By.ID,"com.android.mms:id/action_compose_new"))
    base.send_ele((By.ID,"com.android.mms:id/recipients_editor"),"13934352119")
    # 等待
    time.sleep(3)
    # 退出驱动
    driver.quit()


