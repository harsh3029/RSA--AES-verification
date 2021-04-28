#AUTHOR :: HARSHIT KAPOOR

# Import socket module
import socket
import aes_en
import rsa
import sys
host = '127.0.0.1'

	# Define the port on which you want to connect
port = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)


def Main():

	# connect to server on local computer
	s.connect((host,port))
	# message you send to server
	message = "Send server public key"

	while True:

		# message sent to server
		s.send(message.encode('ascii'))

		# messaga received from server
		data = s.recv(1024)
		server_key = str(data.decode('ascii'))
		# print the received message
		# here it would be a reverse of sent message
		print('Public key received from the server :',str(data.decode('ascii')))

		# ask the client whether he wants to continue
		ans = input('\nDo you want to continue(y/n) :')
		if ans == 'y':

			while True:

				plaintext = int(input("\n\nMESSAGE	 : "))

				key = int(input("KEY 	 : "))

				aes_en.keyExp(key)
				#assert encrypt(plaintext) == ciphertext
				ciphertext = str(aes_en.aes_encrypt(plaintext))
				#e,n public key parameters
				e,n = map(int,input("PUBLIC KEY PARAMETERS (e,n)	: ").split(","))
				#d private key parameter
				d = int(input("PRIVATE KEY PARAMETER (d)	: "))
				#encrypting secret key
				encKey = rsa.RSA(key,server_key,n)
				print("ENCRYPTED SECRET KEY		:",encKey)
				print("CIPHER TEXT	 :", ciphertext)

				#message hash
				digest = rsa.Digest(plaintext)
				#convert digest to ascii
				digest1 = rsa.conv_digest_ascii(digest)
				print("DIGEST 	:",digest1)
				#client signature generation
				client_sign = rsa.RSA(digest1[6],d,n)
				print("DIGITAL SIGNATURE : ",client_sign)

				file = [ciphertext,encKey,client_sign,n,e]
				s.send(file[0].encode('ascii'))
				s.send(file[1].encode('ascii'))
				s.send(file[2].encode('ascii'))
				s.send(str(file[3]).encode('ascii'))
				s.send(str(file[4]).encode('ascii'))


		else:
			break
	# close the connection
	s.close()


if __name__ == '__main__':
    Main()
	