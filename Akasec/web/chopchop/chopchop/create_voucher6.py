import asyncio
import websockets
import json

async def get_voucher():
	uri = "ws://159.223.233.161/socket.io/?EIO=4&transport=websocket"
	custom_headers = {
		"Connection": "Upgrade",
		"Upgrade": "websocket",
		"Host": "159.223.233.161",
		"Content-Type": "application/json",
		"Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MzA4LCJlbWFpbCI6ImxrbjN0cmVAY2hvcGNob3Aub3JnIiwicm9sZSI6InJlY3J1aXQiLCJpYXQiOjE2OTg1Nzg0MjgsImV4cCI6MTY5ODU4MjAyOH0._PaMLfZ9l_KTrVeVF7JpBD6DPRG4Ej5ZIt_HzeiXJhI",
		"Upgrade-Insecure-Requests": "1"
}
	async with websockets.connect(uri , extra_headers=custom_headers) as ws:
		generate_event = json.dumps({"event": "generate"})
	await ws.send(generate_event)
	while True:
		response = await ws.recv()
		voucher_data = json.loads(response)
		voucher = voucher_data['voucher']
		print("Received Response:", voucher)
		break

asyncio.get_event_loop().run_until_complete(get_voucher())
