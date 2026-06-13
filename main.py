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

if __name__ == "__main__" :
    app() 