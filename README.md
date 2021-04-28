# RSA-AES-verification
The project uses Simple AES for encryption and decryption, RSA algorithm for digital signature verification.

# THEORY

## Block diagram for Simple AES used here.
<br>

![output](https://github.com/harsh3029/images/blob/11f10993c629cfeaf1737a7498b0ee30757cd919/Screenshot%20(59).png)

<br>

## Block diagram for the project.

<br>

![output](https://github.com/harsh3029/images/blob/6277c194b51fc05ab6edbaf42029098a97a92f08/Screenshot%20(60).png)


# NOTE
1) The Plaintext and cipher key should be Integer.<br>
2) The Public and private key parameters (p and q) should be distinct prime numbers for both server and client.<br>
3) For a secure RSA Implementation, p and q should be selected greater than 100.<br>
4) server.py should be run before client.py.<br>

# Project Workflow
<ul>
  <li>
    Client inputs: Message, Secret Key, Public and Private key parameters for Client
  </li>
  <li>
    Server Inputs: Public and Private key parameters for Server. 
  </li>
  <br>
</ul>
<ul>
<b><u>Message Flow:</u></b> <br>
  <li>
    Client requests for public key of server.
  </li>
  <li>
    Server sends the public key.
  </li>
  <li>
    Client sends Ciphertext, Encrypted secret key, Client Signature, Client public key.
  </li>
</ul>
<ul>
<br>
<b><u> Client side computation: </u></b><br>
  <li>
    Create Client signature through RSA algorithm, taking Digest from Hash algorithm and client private key as input.
  </li>
  <li>
    Create Ciphertext through the AES variant, taking Message and Secret key as input.
  </li>
  <li>
    Encrypt Secret key with RSA algorithm, taking Secret key and Server Public key as input.
  </li>
<br>
</ul>
<ul>
<b><u>Server side Computation:</u></b><br>
  <li>
    Decrypt Secret key using RSA algorithm 
  </li>
  <li>
    Decrypt ciphertext using AES variant
  </li>
  <li>
    Create message digest
  </li>
  <li>
    Verify Client Signature
  </li>
</ul>

# OUTPUT

![output](https://github.com/harsh3029/images/blob/beae7ed138acec70ca91500c11b3aee96187398e/Screenshot%20(60).png)
