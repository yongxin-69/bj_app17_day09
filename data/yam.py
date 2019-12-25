import os
w = os.getcwd()+os.sep+"data.yml"
import yaml
with open(os.getcwd()+os.sep+"data.yaml","r",encoding="utf8") as f:
    a = []
    data = yaml.safe_load(f)
    print(data,type(data))

    print(w)
with open(os.getcwd()+os.sep+"data.yml","w",encoding="utf8") as f:
    data = {'info': {'name': 'l', 'phone': 's'}, 'add': {'name': 'l', 'phone': 's', 'detail': 'TBD'}}
    yaml.safe_dump(data,f)
