import hashlib 
from core.hash_bytes import hash_bytes

def hash_text(text) : 

    encoded_text = text.encode()

    return hash_bytes(encoded_text)
