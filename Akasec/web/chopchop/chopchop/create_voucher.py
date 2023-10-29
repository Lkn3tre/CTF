import socketio
import requests

# Create a socket.io client

sio = socketio.Client()

# Define a function to handle the 'generate' event
@sio.on('generate')
def generate(data):
    voucher = data.get('voucher')
    if voucher:
        print(f"Received voucher: {voucher}")
    else:
        print("No voucher received")

# Connect to the web app
web_app_url = 'http://159.223.233.161/socket.io'
custom_headers ={'Cookies':'token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjkyLCJlbWFpbCI6ImFhYWFhYWFhQGFhYWFhYWFhLmNvbSIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4NTUyMTU3LCJleHAiOjE2OTg1NTU3NTd9.f43OOlgvVewUO2Z_fuMPtU4CDui9bIrt7IcgaDOCGF4','Upgrade-Insecure-Requests': 1}

try:
    sio.connect(web_app_url)
    # Emit the 'generate' event to request a voucher
    sio.emit('generate',headers=custom_headers)

    # Wait for a response
    sio.sleep(5)  # You can adjust the duration as needed

    # Disconnect from the web app
    sio.disconnect()
except Exception as e:
    print(f"Error: {str(e)}")


