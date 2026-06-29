from hashcli.core.hash_text import hash_text

def test_hash_text_md5():
    result = hash_text("hello")

    assert result["MD5"] == "5d41402abc4b2a76b9719d911017c592" 