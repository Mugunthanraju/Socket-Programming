""" Assignment 2
Computer Networks
server.py
"""

import socket
import lzma

#constants
tostore = "ser_file_sent.xz"
host = socket.gethostname()
print(host)
port = 12345

#opening the socket
s = socket.socket() 

#binding it to the port, "" specifies connection allowed from different systems within same network
s.bind(("", port))			

#setting the socket to listen
s.listen(5)
print("Server Online")


#Whie true specifies that server remains on irrespective
while True:
	#connecting to client
	c, addr = s.accept()
	print('\n****************New Client connected : ', addr)


	#opening a new file to store compressed data
	f = lzma.LZMAFile(tostore, mode="wb")


	#recieving file to compress
	print("\nReceiving file to compress...")
	#recieve uncompressed packets
	pack = c.recv(1024)
	while (pack):
		print ("Receiving file to compress...")
		#lzma compress and writes the data onto our file during write() command
		f.write(pack)
		pack = c.recv(1024)
	f.close()
	print ("Done Receiving file to compress")


	#opening the complete compressed file to return to client
	f = open(tostore,'rb')
	print ('\nSending compressed file...')
	#reading packets from file
	pack = f.read(1024)
	while (pack):
		print ('Sending compressed file...')
		#sending the compressed data
		c.send(pack)
		pack = f.read(1024)
	f.close()
	print ("Done Sending compressed file.")


	#closing the connection to client
	c.close()


#closing the socket
s.close()     