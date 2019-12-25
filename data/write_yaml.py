import os

import yaml
w = os.getcwd()+os.sep+"data.yml"
# a 追加模式  w 覆盖模式
with open(os.getcwd()+os.sep+"data.yml","w",encoding="utf8") as f:
    data = {'info': {'name': '你好', 'phone': 's'}, 'add': {'name': '你好', 'phone': 's', 'detail': 'TBD'}}
    yaml.safe_dump(data,f,encoding="utf8",allow_unicode=True)
