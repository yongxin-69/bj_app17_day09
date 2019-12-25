import pytest,sys,os


from Base.detData import GetData








# def read_data():
#
#     with open("./data/data1.yaml","r",encoding="utf8") as f:
#         a = []
#         data = yaml.safe_load(f)
#         print(data)
#         for i in data.values():
#             a.append(tuple(i))
#     print(a)
#     return a
def get_sum_data():
    data = GetData().read_data("data1.yaml")
    w = []
    for i in data.values():
        w.append(tuple(i))
    return w
class Test01:

    @pytest.mark.parametrize("a,b,c",get_sum_data())
    def test_01(self,a,b,c):
        print("{}+{}={}".format(a,b,c))
        assert a+b ==c