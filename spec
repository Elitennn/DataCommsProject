

##Overview
This is a st of jve classes that implements
1)a packet transmission end point (sender and athe receiver)
2)the packet
3)a main class for testing

##Details of the data packet in our protocol
1)Header which contains: sequence number and checksum for error detection 
2)Payload -which contains a part of the entire message

each data packet is 64 characters in size 

**header** 6 characters 
first 3 = sequence number eg '000'-'999' -maximum 1000 packets message size
next 3=checksum eg 0-999

**Payload** = actual payload eg '123123123123...' which represents '{{{{'
so each set of 3 numbers represens the ascii value of a character.
add a NULL character to the end to get a round 64 (2^6) size.

##The packet clas


### data coms macjine class
This class has both sending and recieving powers.
In the sender the message is broken into packets, The sequence number and checksum is added.
IN the reciev er each packet is checked for errors (asked  to be resent by sequence number if there are errors)
then the message is resassembled in order and assed back to the pagram.
