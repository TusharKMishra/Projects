from Crypto.Cipher import AES
import base64
import os

class EncryptionManager:
    def __init__(self, key):
        self.key = key.rjust(32)[:32]

    def encrypt(self, plain_text):
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
        return base64.b64encode(nonce + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_text):
        encrypted_data = base64.b64decode(encrypted_text)
        nonce = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        cipher = AES.new(self.key.encode('utf-8'), AES.MODE_EAX, nonce=nonce)
        plain_text = cipher.decrypt(ciphertext).decode('utf-8')
        return plain_text
