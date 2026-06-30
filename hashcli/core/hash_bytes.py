import hashlib

def hash_bytes(data, algorithms) :
    results = {} 

    for algorithm in algorithms :
        hash_object = hashlib.new(algorithm)
        hash_object.update(data)
        results[algorithm.upper()] = hash_object.hexdigest()

    return results

    