import hashlib
from core.hash_bytes import hash_bytes

def hash_file(path) :
    with open(path, "rb") as file :
        data = file.read() 

        return hash_bytes(data)

