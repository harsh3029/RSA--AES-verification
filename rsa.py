#AUTHOR :: HARSHIT KAPOOR

import random
import gmpy2
import sys
import hashlib




#gcd return the greatest common devisor of the two nos using Euclidean Algorithm
def gcd(a,b):
	a = abs(a)
	b = abs(b)

	#if a<b then interchange the value of a and b
	if a<b:
		a, b = b, a

	#replace a = b and b = a%b
	while b != 0:
		a, b = b, a%b

	#return the gcd
	return a


def RSA(msg,exp,n):



	#computing d, 1<d<O(n); such that e*d = 1 mod O(n) or d = multiplicativeinverse(e,phin)

	#Public Key = (e,n)
	#Private Key = d

	#encrypting the digest using RSA algorithm CT = m^exp mod n
    enc = pow(int(msg),int(exp),int(n))
    return str(enc)

def conv_digest_ascii(msg):
    #converting the digest to its ascii value
    m = ''
    for i in str(msg):
	    m = m+str(ord(i))
    return m

def Digest(msg):

	#calculating the hash of the message using sha224
	return hashlib.sha224(str(msg).encode()).hexdigest()
