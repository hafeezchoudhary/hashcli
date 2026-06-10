import hashlib

def hash_text(text) :

    algorithms = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512,
    } 

    results = {}
    encoded_text = text.encode()

    for algorithm_name, algorith_function in algorithms.items() :
        results[algorithm_name] = algorith_function(encoded_text).hexdigest()

    return results

    
if __name__ == "__main__" :
    text = input()
    print(hash_text(text)) 
