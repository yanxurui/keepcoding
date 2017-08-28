import socket, ssl
import pprint

context = ssl.create_default_context(cafile='cert.pem')

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname="mononoke.com")
conn.connect(("mononoke.com", 4433))

cert = conn.getpeercert()
pprint.pprint(cert)

while True:
    data = raw_input('enter message(enter q to quit)>')
    conn.sendall(data)
    if data == 'q':
        break
    print(conn.recv(1024))
