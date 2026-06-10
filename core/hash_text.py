import hashlib

def hash_text(text) :

    # hashed_sha256 = hashlib.sha256(text.encode()).hexdigest() 
    # hashed_md5 = hashlib.md5(text.encode()).hexdigest()
    # hashed_sha1 = hashlib.sha1(text.encode()).hexdigest()
    # hashed_sha512 = hashlib.sha512(text.encode()).hexdigest() 

    # return {
    #     "SHA256": hashed_sha256,
    #     "MD5": hashed_md5,
    #     "SHA1": hashed_sha1,
    #     "SHA512": hashed_sha512
    # } 

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
