import requests
import socketio
# Define a function to handle the 'generate' event
def generate(data):
    voucher = data.get('voucher')
    if voucher:
        print(f"Received voucher: {voucher}")
    else:
        print("No voucher received")


url = 'http://159.223.233.161/api/shop/isAdmin'
cookie={
	'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA4LCJlbWFpbCI6ImxrbjN0cmVAY2hvcGNob3Aub3JnIiwicm9sZSI6InJlY3J1aXQiLCJpYXQiOjE2OTg1NzI3MDAsImV4cCI6MTY5ODU3NjMwMH0.bmo33jpHNOWLyaRBxUkZsFcI0-I0mbXaE0BXfb8ksX8'}
header={
	'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA4LCJlbWFpbCI6ImxrbjN0cmVAY2hvcGNob3Aub3JnIiwicm9sZSI6InJlY3J1aXQiLCJpYXQiOjE2OTg1NzI3MDAsImV4cCI6MTY5ODU3NjMwMH0.bmo33jpHNOWLyaRBxUkZsFcI0-I0mbXaE0BXfb8ksX8'}

response = requests.get(url,cookies=cookie,headers=header)
"""
if response.status_code == 200:
    sio = socketio.Client()

    @sio.on('generate')
    def on_generate(data):
        generate(data)

    sio.connect(url)
    sio.sleep(5)

    sio.disconnect()
else:
    print(f"{response.status_code}")
"""
print(response.text)

