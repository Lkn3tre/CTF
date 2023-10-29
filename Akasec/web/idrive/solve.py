import requests

url = 'http://159.223.230.26:4242/%F0%9F%93%9D'
data = {
		"firstname":"(7*7)",
		"lastname":"3*3",
		"address":"3*3",
		"birthday":"2023/10/1",
		"debt":"10",
		"balence":"3*3",
		"city":"(3*3)"
}
res = requests.post(url,json=data,headers={"Content-Type": "application/json"})
print(res.text)
