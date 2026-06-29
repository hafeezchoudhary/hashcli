import hashlib

def verify_hash(results, target_hash) :
    
    for algorithm_name, hash_value in results.items() :

        if hash_value == target_hash : 
            return {
                "match": True,
                "algorithm": algorithm_name
            }
            break

    return {
        "match": False,
        "algorithm": None
    }
