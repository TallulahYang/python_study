import socket
s=socket.socket()

s.connect(('192.168.1.41',3000))
data=s.recv(512)
print ('the data received is\n    ',data)
s.send('hi I am client')
while True:
    text = str(raw_input('> please input:\n'))
    s.send(text)
    if text == 'q':
        s.close()
        break