import hashlib

def hash_text(text) :

    hashed_sha256 = hashlib.sha256(text.encode()).hexdigest()
    hashed_md5 = hashlib.md5(text.encode()).hexdigest()
    hashed_sha1 = hashlib.sha1(text.encode()).hexdigest()
    hashed_sha512 = hashlib.sha512(text.encode()).hexdigest()

    return {
        "SHA256": hashed_sha256,
        "MD5": hashed_md5,
        "SHA1": hashed_sha1,
        "SHA512": hashed_sha512
    }

