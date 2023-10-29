import socketio
import requests

# Define a function to handle the 'generate' event
def generate(data):
    voucher = data.get('voucher')
    if voucher:
        print(f"Received voucher: {voucher}")
    else:
        print("No voucher received")

# Make an HTTP request to the web app with custom headers
web_app_url = 'http://159.223.233.161:3000/socket.io/'
cookie = {'token':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA4LCJlbWFpbCI6ImxrbjN0cmVAY2hvcGNob3Aub3JnIiwicm9sZSI6InJlY3J1aXQiLCJpYXQiOjE2OTg1Nzg0MjgsImV4cCI6MTY5ODU4MjAyOH0._PaMLfZ9l_KTrVeVF7JpBD6DPRG4Ej5ZIt_HzeiXJhI'}
custom_headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA4LCJlbWFpbCI6ImxrbjN0cmVAY2hvcGNob3Aub3JnIiwicm9sZSI6InJlY3J1aXQiLCJpYXQiOjE2OTg1Nzg0MjgsImV4cCI6MTY5ODU4MjAyOH0._PaMLfZ9l_KTrVeVF7JpBD6DPRG4Ej5ZIt_HzeiXJhI','Upgrade-Insecure-Requests': '1','Connection':'keep-alive'}

response = requests.get(web_app_url, cookies=cookie,headers=custom_headers)
print(response.text)
if response.status_code == 200:
    # Create a socket.io client
    sio = socketio.Client()

    @sio.on('generate')
    def on_generate(data):
        generate(data)

    sio.connect(web_app_url)

    # Wait for a response
    sio.sleep(5)  # You can adjust the duration as needed

    # Disconnect from the web app
    sio.disconnect()
else:
    print(f"HTTP request failed with status code {response.status_code}")
