

def get_driver(pac,act):
    from appium import webdriver
    import time
    # 创建驱动对象
    d = {}
    d["platformName"]= "Android"
    d["platformVersion"]= "5.1"
    d["deviceName"]= "模拟器"
    d["appPackage"]= pac
    d["appActivity"]=act
    d["resetKeyboard"]=True
    d["unicodeKeyboard"]=True

    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)








