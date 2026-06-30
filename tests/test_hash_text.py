from hashtool.core.hash_text import hash_text

def test_hash_text_SHA1():
    result = hash_text("नमस्ते")

    assert result["SHA1"] == "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d" 

def test_hash_text_md5():
    result = hash_text("hello")

    assert result["MD5"] == "5d41402abc4b2a76b9719d911017c592" 

def test_hash_text_SHA256():
    result = hash_text("")

    assert result["SHA256"] == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824" 

def test_hash_text_SHA512():
    result = hash_text("54533")

    assert result["SHA512"] == "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043" 