from core.hash_text import hash_text 
from output.console_output import display_hash_table 
from core.hash_file import hash_file
from core.verify_hash import verify_hash
import typer


app = typer.Typer()
@app.command() 
def text(text: str) :
    text_result = hash_text(text)  
    display_hash_table(text_result) 

@app.command()
def file(path: str) :
    file_result = hash_file(path) 
    display_hash_table(file_result)

@app.command(name = "verify-file") 
def verify_file(path: str, target_hash: str) :
    file_hash_result = hash_file(path)  
    verification_result = verify_hash(file_hash_result, target_hash) 
    print(verification_result ) 

@app.command(name = "verify-text") 
def verify_text(text:str, target_hash:str) :
    text_hash_result = hash_text(text)
    verification_result = verify_hash(text_hash_result, target_hash)
    print(verification_result) 

if __name__ == "__main__" :
    app() 