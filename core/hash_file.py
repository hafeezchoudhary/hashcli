import hashlib

def hash_file(path) :
    with open(path, "rb") as file :
        data = file.read() 

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

        file.close() 

if __name__ == "__main__" :
    result = hash_file("tests/sample.txt")
    print(result) 
