from core.hash_text import hash_text 
from output.console_output import display_hash_table 
from core.hash_file import hash_file

text = input()
text_result = hash_text(text) 
file_result = hash_file("tests/sample.txt")
display_hash_table(text_result)  
display_hash_table(file_result)  

