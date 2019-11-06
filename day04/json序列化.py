

import json
info = {
    "name":"yanzhuang",
    "age":22
}
f = open("test.txt","w")
f.write(json.dumps(info))
f.close()