import os
import yaml


class GetData:


    def read_data(self,yml_name):
        w = os.getcwd() + os.sep + "data" + os.sep + yml_name

        with open(w, "r", encoding="utf8") as f:

            return yaml.safe_load(f)



if __name__ == '__main__':
    pass

