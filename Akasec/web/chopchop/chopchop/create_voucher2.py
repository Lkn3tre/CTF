import websocket
import json

# Define the WebSocket URL (replace with your actual WebSocket URL)
websocket_url = 'ws://159.233.233.161:3000/socket.io/'
# Function to handle messages from the WebSocket server
def on_message(ws, message):
    data = json.loads(message)
    event = data['event']

    if event == 'generate':
        voucher = data.get('voucher')
        if voucher:
            print(f"Received voucher: {voucher}")
        else:
            print("No voucher received")
custom_header={"Cookie":"token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Mjc1LCJlbWFpbCI6ImxrbjN0cmVlQGNob3BjaG9wLm9yZyIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4NTQ3NzM3LCJleHAiOjE2OTg1NTEzMzd9.ar5lZAN2LaprUXJd1I15uQ60bWuOzlFpDOlX7fDFqTY","Upgrade-Insecure-Requests":1}
# Create a WebSocket connection
ws = websocket.WebSocketApp(websocket_url, on_message=on_message,header=custom_header)

# Start the WebSocket connection
ws.run_forever()
