from core.hash_text import hash_text 
from output.console_output import display_hash_table 
from core.hash_file import hash_file
from core.verify_hash import verify_hash

text = input()
text_result = hash_text(text) 
file_result = hash_file("tests/sample.txt")
display_hash_table(text_result)  
display_hash_table(file_result)  
verify_result = verify_hash(file_result, "64ec88ca00b268e5ba1a35678a1b5316d212f4f366b2477232534a8aeca37f3c")
verify_result = verify_hash(text_result, "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824")
print(verify_result) 


