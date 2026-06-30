def detect_algorithm(hash_value) :
    
    hash_value = hash_value.strip()
    length = len(hash_value)

    HASH_LENGTHS = {
        32: ["MD5"],
        40: ["SHA1"],
        64: ["SHA256"],
        128: ["SHA512"],
    }

    algorithms = HASH_LENGTHS.get(length, ["Unknown"])
    return {
        "length": length,
        "algorithms": algorithms,
    } 