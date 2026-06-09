from core.hash_text import hash_text 
from output.console_output import display_hash_table 

text = input()
result = hash_text(text) 
output = display_hash_table(result)
