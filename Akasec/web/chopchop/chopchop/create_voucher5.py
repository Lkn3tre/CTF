import websocket
import json

url = "ws://159.223.233.161/socket.io/?EIO=4&transport=websocket"

ws = websocket.create_connection(url)

# Send an event to trigger 'generate'
generate_event = json.dumps({"event": "generate"})
ws.send(generate_event)

while True:
    response = ws.recv()
    if "generate" in response:
        # Handle the 'generate' event response, which should contain the voucher
        voucher_data = json.loads(response)
        voucher = voucher_data.get("voucher")
        print("Received Voucher:", voucher)
        break  # Exit the loop after receiving the voucher

# Receive the response from the server
#response = ws.recv()

# Handle the response
#print("Response:", response)

ws.close()
