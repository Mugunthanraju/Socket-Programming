""" Assignment 2
Computer Networks
client.py
"""

import socket

#constants
port = 12345
tosend = 'check.py'
torec = 'cli_file_recv.xz'
host = socket.gethostname()	#Change to sever IP Address if different systems on same network


#Creating a socket and connecting to server
s = socket.socket()
s.connect((host, port))


#opening file to send
f = open(tosend,'rb')
#Sending file to compress
print ('\n Sending file to compress...')
pack = f.read(1024)
while(pack):
	print ('Sending file to compress...')
	s.send(pack)
	pack = f.read(1024)
f.close()
print ("Done Sending file to compress")


#Shutting down the sending capabilities of client socket
s.shutdown(socket.SHUT_WR)


#Opening a new file to recieve the compressed file
f = open(torec,'wb')
print ("\n Receiving compressed file...")
#Recieving the compressed file
pack = s.recv(1024)
while(pack):
	print ("Receiving compressed file...")
	f.write(pack)
	pack = s.recv(1024)
f.close()
print ("Done Receiving compressed file")


# Closing the socket
s.close()