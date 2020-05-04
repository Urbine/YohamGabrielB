# This simple program reesembles a socket to get data off a web page.
# I initialised the socked and displayed the headers and contents in execution.
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n' .encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1 ) :
        break
    print(data.decode())
mysock.close() # Now the connection is closed, because the file reached it's end.
