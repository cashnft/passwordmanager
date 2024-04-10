from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import os

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)
def generate_salt() -> bytes:
    return os.urandom(16)
def encrypt_message(message: str, key: bytes) -> bytes:
    f = Fernet(key)
    encoded_message = message.encode()
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message
def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
