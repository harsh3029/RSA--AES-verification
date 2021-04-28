#AUTHOR :: HARSHIT KAPOOR

# import socket programming library
import socket
import aes_de
import rsa

# import thread module
from _thread import *

import threading

print_lock = threading.Lock()

# thread function
def threaded(c):
    while True:

        # data received from client
        data = c.recv(1024)
        if not data:
            print('Bye')

            # lock released on exit
            print_lock.release()
            break

        pb_key =(input('\nSERVER PUBLIC KEY   : '))
        # send back reversed string to client
        c.send(pb_key.encode())
        # print(data2)
        data0 = c.recv(1024)
        data1 = c.recv(1024)
        data2 = c.recv(1024)
        data3 = c.recv(1024)
        data4 = c.recv(1024)

        #assign value to variables
        ciphertext = data0.decode('ascii')
        en_c_key = str(data1.decode('ascii'))
        client_sign = str(data2.decode('ascii'))
        n = str(data3.decode('ascii'))
        e = str(data4.decode('ascii'))
        #server private key
        s_p_key = int(input("SERVER PRIVATE KEY  : "))

        #secret key calculated
        s_key = rsa.RSA(en_c_key,s_p_key,n)
        print("DECRYPTED SECRET KEY :",s_key)
        #giving secret key as input
        aes_de.keyExp(int(s_key))
        #finding plain text
        ptext = str(aes_de.aes_decrypt(int(ciphertext)))
        print("DECRYPTED MESSAGE    :",ptext)
        #finding digest using hash algorithm
        digest = rsa.conv_digest_ascii(rsa.Digest(ptext))

        print("MESSAGE DIGEST       :",digest)
        #using RSA algorithm
        digest__ = (rsa.RSA(client_sign,e,n))
        print("VERIFICATION CODE :",digest__)
        num  = digest[6]
        #if decrypted digest == calculated hash then the sender is verified else message has been tampered with
        if digest__ == num :
            print("\n\nSender Verified.")
        else:
            print("\n\nNot able to verify the sender and/or message has been tampered.")

    # connection closed
    c.close()




if __name__ == '__main__':
    host = ""

	# reverse a port on your computer
	# in our case it is 12345 but it
	# can be anything
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket binded to port", port)

	# put the socket into listening mode
    s.listen(5)
    print("socket is listening")

	# a forever loop until client wants to exit
    while True:

		# establish connection with client
        c, addr = s.accept()

		# lock acquired by client
        print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])

		# Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()