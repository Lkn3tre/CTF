import asyncio
import websockets

async def connect_to_websocket_server():
    uri = "ws://159.223.233.161/socket.io/?EIO=2&transport=polling:3000"  # Replace with your WebSocket server URL
    custom_header={"Authorization" : "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzE1LCJlbWFpbCI6ImxrbjN0cmVAYS5jb20iLCJyb2xlIjoicmVjcnVpdCIsImlhdCI6MTY5ODU3NDk3NSwiZXhwIjoxNjk4NTc4NTc1fQ.hk5DqcKpMvuSUUbivNtb-MpvjnWoSmb49WhJVxImTZs"}
    async with websockets.connect(uri,extra_headers=custom_header) as websocket:
        print("Connected to the WebSocket server")

        while True:
            message = input("Enter a message to send (or type 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            await websocket.send(message)
            response = await websocket.recv()
            print(f"Received from server: {response}")

asyncio.get_event_loop().run_until_complete(connect_to_websocket_server())
