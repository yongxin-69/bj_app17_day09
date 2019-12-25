from selenium.webdriver.common.by import By


class PageElement:
    xinjian = (By.ID,"com.android.mms:id/action_compose_new")
    lianxiren = (By.ID,"com.android.mms:id/recipients_editor")
    wenben = (By.ID,"com.android.mms:id/embedded_text_editor")
    fasong = (By.ID,"com.android.mms:id/send_button_sms")
    duanyan = (By.ID,"com.android.mms:id/text_view")
    shanchu = (By.XPATH,"//*[contains(@text,'appium')]")
    shanchu1 = (By.XPATH,"//*[contains(@text,'删除')]")
    queren = (By.ID, "android:id/button1")


