import socket
import time
import pickle
import random

#constants
tosend = 'check.py'
torec = 'cli_file_recv.xz'
# host = socket.gethostname()	#Change to sever IP Address if different systems on same network
# host = ''
transmit_window = 7
time_out = 1e-2
network_status = 0
buffer = []
clock = 0
pack_counter = 0
packets = 1000
first = False

currently_expected = 0
reciever_expected = 0

class Frame:
	def __init__(self, seq, time, data):
		self.seq = seq
		self.time = time
		self.data = data

	def encode(self):
		return pickle.dumps(self)
	
	@staticmethod
	def decode(s):
		return pickle.loads(s)


def delay():
	n = 1e6
	while n >= 0:
		n = n - 1

def send():
	global transmit_window, time_out, buffer, clock, pack_counter, packets, first
	# f = open(tosend,'rb')
	if ( pack_counter > packets ):
		return
	print ('\n Sending packets...')
	delay()
	pack = random.randint(100000,1000000)
	i = 0
	while(pack):
		print ('Sending file to compress...')
		# s.send()
		if (len(buffer)!= 0):
			for k in range(len(buffer)):
				buffer[k].seq = k
			i = len(buffer)
		# pack = f
		if (len(buffer) < transmit_window + 1):
			buffer.append(Frame(i, time.time(), pack))
		else:
			for i in buffer:
				# if (random.random() <= 0.9):
				if True:
					print('sending ..', i.seq)
					s.send(i.encode())
			# s.shutdown(socket.SHUT_WR)
							
			print('waiting for ack')
			clock = time.time()
			
			currently_expected = 0
			data = s.recv(4096)
			frm = Frame.decode(data)

			while currently_expected < transmit_window + 1 and (time.time() - clock < time_out):
				if frm.seq == currently_expected:
					buffer.remove(0)
					currently_expected += 1
					pack_counter+=1
				else :
					# s.shutdown(socket.SHUT_RD)
					send()
			
			if (currently_expected < transmit_window + 1):
				print('timed out')
				# s.shutdown(socket.SHUT_RD)
				send()

		i = (i + 1) % (transmit_window + 1)
	# f.close()

def recieve():
	global transmit_window, time_out, buffer, clock, pack_counter, packets, first
	print('receiving packets')
	reciever_expected = 0
	data = s.recv(4096)
	frm = Frame.decode(data)
	frm_seq = frm.seq

	if (frm_seq == reciever_expected):
		if not first:
			print(" First Packet recieved : " + str(reciever_expected))
			first = True
		else:
			print("Packet recieved : " + str(reciever_expected))	
			frm.data = 'ack'
			frm.time = time.time()
			s.send(frm)
		reciever_expected += 1
	else:
		print('bad sequence...')
		recieve()
		# s.shutdown(socket.SHUT_RD)



# def prob():
# 	pass


# #Creating a socket and connecting to server


# #opening file to send
# f = open(tosend,'rb')
# #Sending file to compress
# print ('\n Sending file to compress...')
# pack = f.read(1024)
# while(pack):
# 	print ('Sending file to compress...')
# 	s.send(pack)
# 	pack = f.read(1024)
# f.close()
# print ("Done Sending file to compress")


# #Shutting down the sending capabilities of client socket
# s.shutdown(socket.SHUT_WR)


# #Opening a new file to recieve the compressed file
# f = open(torec,'wb')
# print ("\n Receiving compressed file...")
# #Recieving the compressed file
# pack = s.recv(1024)
# while(pack):
# 	print ("Receiving compressed file...")
# 	f.write(pack)
# 	pack = s.recv(1024)
# f.close()
# print ("Done Receiving compressed file")


# Closing the socket


# main
host =""
port = 12344

s = socket.socket()
s.connect((host, port))

# s.bind((host, port))
# print("Server binded at port: ", str(port))

# s.listen(1)
# print("Socket is listening")

# client_socket, address = s.accept()
# print("Got connection from ", str(address))
send()
s.close()
