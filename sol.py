import json
import os

endpoint = "curl --header 'token: oSgDmnvLL9GwKZwFoiKHJE' https://www.find.foo/api/challenge"
# data = os.system(endpoint)
# print data

import subprocess
result = os.popen(endpoint).read()
data = json.loads(result)

print data['challenge']