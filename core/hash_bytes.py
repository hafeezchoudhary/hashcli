import hashlib

def hash_bytes(data) :
    results = {}
    
    algorithms = {
        "SHA1": hashlib.sha1,
        "MD5": hashlib.md5,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512,
    } 

    for algorithm_name, algorithm_function in algorithms.items() :
        results[algorithm_name] = algorithm_function(data).hexdigest()

    return results

    