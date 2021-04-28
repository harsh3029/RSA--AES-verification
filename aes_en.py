#AUTHOR :: HARSHIT KAPOOR

import sys
import rsa


sBox  = [0x9, 0x4, 0xa, 0xb, 0xd, 0x1, 0x8, 0x5,
         0x6, 0x2, 0x0, 0x3, 0xc, 0xe, 0xf, 0x7]

# Round keys: K0 = w0 + w1; K1 = w2 + w3; K2 = w4 + w5
w = [None] * 6

def mult(p1, p2):
    """Multiply two polynomials in GF(2^4)/x^4 + x + 1"""
    p = 0
    while p2:
        if p2 & 0b1:
            p ^= p1
        p1 <<= 1
        if p1 & 0b10000:
            p1 ^= 0b11
        p2 >>= 1
    return p & 0b1111
 
def intToVec(n):
    """Convert a 2-byte integer into a 4-element vector"""
    return [n >> 12, (n >> 4) & 0xf, (n >> 8) & 0xf,  n & 0xf]            
 
def vecToInt(m):
    """Convert a 4-element vector into 2-byte integer"""
    return (m[0] << 12) + (m[2] << 8) + (m[1] << 4) + m[3]
 
def addKey(s1, s2):
    """Add two keys in GF(2^4)"""  
    return [i ^ j for i, j in zip(s1, s2)]
     
def sub_NibList(sbox, s):
    """Nibble substitution function"""
    return [sbox[e] for e in s]
     
def shiftRow(s):
    """ShiftRow function"""
    return [s[0], s[1], s[3], s[2]]
 
def keyExp(key):
    """Generate the three round keys"""
    def sub2Nib(b):
        """Swap each nibble and substitute it using sBox"""
        return sBox[b >> 4] + (sBox[b & 0x0f] << 4)
 
    Rcon1, Rcon2 = 0b10000000, 0b00110000
    w[0] = (key & 0xff00) >> 8
    # print("Round key K0: " + str(w[0]))
    w[1] = key & 0x00ff
    w[2] = w[0] ^ Rcon1 ^ sub2Nib(w[1])
    w[3] = w[2] ^ w[1]
    w[4] = w[2] ^ Rcon2 ^ sub2Nib(w[3])
    w[5] = w[4] ^ w[3]

def aes_encrypt(ptext):
    """Encrypt plaintext block"""
    def mixCol(s):
        return [s[0] ^ mult(4, s[2]), s[1] ^ mult(4, s[3]),
                s[2] ^ mult(4, s[0]), s[3] ^ mult(4, s[1])]    
    #round 1
    state = intToVec(((w[0] << 8) + w[1]) ^ ptext)
    s1 = sub_NibList(sBox, state)
    sh1 = shiftRow(s1)
    state = mixCol(sh1)
    # print("Round 1 Substitute nibble " + str(s1))
    # print("Round 1 shift row" + str(sh1))
    # print("Round 1 mix column " + str(state))

    state = addKey(intToVec((w[2] << 8) + w[3]), state)
    # print("After Round 1 add key: " + str(state))
    # print("Round key K1: " + str((w[2] << 8) + w[3]))

    #round2
    s2 = sub_NibList(sBox, state)
    state = shiftRow(s2)
    # print("Round 2 Substitute nibble " + str(s2))
    # print("Round 2 shift row" + str(state))
    state_ = addKey(intToVec((w[4] << 8) + w[5]), state)
    # print("After Round 1 add key: " + str(state_))
    # print("Round key K1: " + str((w[4] << 8) + w[5]))

    return vecToInt(state_)
