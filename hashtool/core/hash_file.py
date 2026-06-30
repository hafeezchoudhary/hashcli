import hashlib
from hashtool.core.hash_bytes import hash_bytes

def hash_file(path, algorithms = None) :
    if algorithms is None:
        algorithms = ["md5", "sha1", "sha256", "sha512"]

    with open(path, "rb") as file :
        data = file.read() 

        return hash_bytes(data, algorithms)

