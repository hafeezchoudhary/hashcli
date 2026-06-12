import hashlib 

def hash_text(text) :

    algorithms = {
        "SHA1": hashlib.sha1,
        "MD5": hashlib.md5,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512,
    } 

    results = {}
    encoded_text = text.encode()

    for algorithm_name, algorithm_function in algorithms.items() :
        results[algorithm_name] = algorithm_function(encoded_text).hexdigest()

    return results 