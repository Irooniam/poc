from Crypto.Cipher import Salsa20
import base64
import logging
logger = logging.getLogger(__name__)

def encrypt(key, cleartext):
    cipher = Salsa20.new(key=key.encode()) 
    ciphertext = cipher.nonce + cipher.encrypt(cleartext.encode())

    #base64 encode so we can easily post data via http
    return base64.b64encode(ciphertext) 

def decrypt(key, encodedtext):
    #first decode64
    decoded = base64.b64decode(encodedtext)
    nonce = decoded[:8]
    ciphertext = decoded[8:]
    cipher = Salsa20.new(key=key.encode(), nonce=nonce)
    cleartext = cipher.decrypt(ciphertext)
    return cleartext
