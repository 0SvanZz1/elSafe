from Crypto.PublicKey import RSA as rsa
import hashlib

def generate_rsa(bits):
    """Generates a RSA key pair

    Parameters
    ----------
    bits : int
        Size of the key pair in bits

    Returns
    -------
    str
        hexadecimal DER value of the private key
    str
        hexadecimal DER value of the public key
    """
    if type(bits) is int and bits > 0:
        privKey = rsa.generate(bits)
        pubKey = privKey.publickey()
        return hashlib.sha256(privKey.exportKey("DER")).hexdigest(), hashlib.sha256(pubKey.exportKey("DER")).hexdigest()