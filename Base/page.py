from Base.detData import GetData
from Page.duanXin import Duan


class Page:
    def __init__(self,driver,yml_name):
        self.driver = driver

    def fsdx(self):
        return Duan(self.driver)



