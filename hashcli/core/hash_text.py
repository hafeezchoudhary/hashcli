import hashlib 
from hashcli.core.hash_bytes import hash_bytes

def hash_text(text, algorithms = None) : 
    if algorithms is None:
        algorithms = ["md5", "sha1", "sha256", "sha512"]

    encoded_text = text.encode()

    return hash_bytes(encoded_text, algorithms)
