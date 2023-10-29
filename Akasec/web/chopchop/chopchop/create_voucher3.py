import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to server')

@sio.event
def disconnect():
    print('Disconnected from server')

@sio.on('generate')
def receive_voucher(data):
    voucher = data.get('voucher')
    print(f'Received Voucher: {voucher}')

if __name__ == '__main__':
    server_ip = 'http://159.223.233.161/socket.io/'  # Replace with the actual server IP
    sio.connect(server_ip)

    try:
        while True:
            pass
    except KeyboardInterrupt:
        sio.disconnect()
