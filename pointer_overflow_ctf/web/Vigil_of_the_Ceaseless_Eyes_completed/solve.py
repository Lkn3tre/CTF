import requests
import base64

x = requests.get('https://nvstgt.com/ManyKin/secret/flag.pdf')
print(x.text)
