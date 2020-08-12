# Socket-Programming

#### Application 1 - File Compression

The client in this application sends files to the server which are compressed using Lempel-Ziv compression technique and sent back to the client.

The client sends the file to be compressed to the server in multiple packets using the connection oriented Transmission Control Protocol. It then waits for an acknowledgement from the server before sending the next packet.
After the server compresses the file, the client again establishes a connection with the server to recieve the compressed file. This time the client receives packets from the server and sends acknowledgements.

The established sockets were working seamlessly and we were getting fully lossless data compression. We were getting about 14% compression after performing Lempel-Ziv compression.
This is an iterative server since queries are handled sequentially as opposed to parallel.


#### Application 2 - Data Link Layer

Implemented Go-back-n protocol
In the go-back-n protocol, then sender continues to send frames till a window size (which is
predetermined) even without ACK packet from the receiver.
The receiver knows the sequence number of whichever frame it is expecting to receive.
If the sequence number of the frame is not equal to the sequence number that the receiver expects, the receiver discards it and resends the ACK for the last “correct” frame it receives.
After the sender has sent every frame (in the window), it will go back to the sequence number of last ACK it received from the receiver and will empty and then refill the window from that frame and continues it.


Both server and client can send packets to the other end of the connection. Let us suppose, for explanation sake, that client wants to send the packets to the server.
We have used python random number generator [0,1] to generate a value for each packet, and if that probability comes out to be greater than p = 0.9 then we drop that packet otherwise the packet is sent on the network.
If the packet was dropped, according to the above procedure, then the client wouldn’t receive an ack for that same.
     
Thus, the go-back-n protocol would come into effect and client would go back to the last packet sent correctly(for which it received an ack, in order) and would send the whole n-window to the receiver again starting from the first packet for which it didn’t receive the ack correctly.
On the other hand, the receiver, when receives a packet, it puts a timestamp on it and sends the ack back to the sender and then again waits for the next packet.
If a packet received by the receiver is wrong (aka out of order) then:
It resets it count and wait for the correct (missed) packet again, followed by all other packets (in-order).
