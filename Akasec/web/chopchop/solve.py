import requests

url = 'http://localhost:3000'
data = {'voucher':'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqdb5552521fa9ebb021a7f3ed687302504a57d2b5d3d448bb43acb4588475c17e'}
cookie = {'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiIxQGNob3BjaG9wLm9yZyIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4ODY0MzA1LCJleHAiOjE2OTg4Njc5MDV9.-_Y0m1J_h954LrFPRYyQuuqtT_n66w_5ygiTXZvdnqA'}
header = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiIxQGNob3BjaG9wLm9yZyIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4ODY0MzA1LCJleHAiOjE2OTg4Njc5MDV9.-_Y0m1J_h954LrFPRYyQuuqtT_n66w_5ygiTXZvdnqA'}
res = requests.post(url+'/shop/redeem',json=data,cookies=cookie,headers=header)

print(res.text)
