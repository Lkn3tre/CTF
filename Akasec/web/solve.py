import requests

url = 'http://localhost:80'
data = {'voucher':'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqdb5552521fa9ebb021a7f3ed687302504a57d2b5d3d448bb43acb4588475c17e'}
cookie = {'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiIxQGNob3BjaG9wLm9yZyIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4ODYzNDU5LCJleHAiOjE2OTg4NjcwNTl9.WVK2qDyvkqqylc-eRC6miTTvOF4ehukFtWWhREpk8a0'}
res = requests.post(url+'/verify',json=data,cookies=cookie)
print(res.text)