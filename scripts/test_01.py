from Base.getDriver import get_driver
from Base.page import Page
import pytest

class Test:
    def setup_class(self):
        self.driver = get_driver("com.android.mms",".ui.ConversationList")
        self.page_obj = Page(self.driver)
        self.page_obj.fsdx().click_xinjian()
        self.page_obj.fsdx().send_lianxiren("13938394119")
    def teardown_class(self):
        self.driver.quit()
    @pytest.mark.parametrize("text",["hello","world","appium"])
    def test_01(self,text):
        self.page_obj.fsdx().send_wenben(text)
        self.page_obj.fsdx().click_fasong()
        assert text in self.page_obj.fsdx().get_duanyan()
    def test_02(self):
        self.page_obj.fsdx().shanchu()
        assert "appium" not in self.page_obj.fsdx().get_duanyan()












