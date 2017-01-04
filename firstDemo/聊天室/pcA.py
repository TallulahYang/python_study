import socket
s=socket.socket()
s.bind(('192.168.1.41',3000))
s.listen(5)
cs,address = s.accept()
print('got connected from',address)
cs.send('hello I am server,welcome')
while True:
    ra=cs.recv(512)
    print(ra)
    if ra=='q':
        cs.close()
        break

