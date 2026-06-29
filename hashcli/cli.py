from hashcli.core.hash_text import hash_text 
from hashcli.output.console_output import display_hash_table 
from hashcli.core.hash_file import hash_file
from hashcli.core.verify_hash import verify_hash
from hashcli.output.verification_output import display_verification_result
import typer 

app = typer.Typer(help="HasCLI - Command-line utility for generating and verifying cryptographic hashes.")
@app.command(help="Generate cryptographic hashes for the provided text input.") 
def text(text: str = typer.Argument(..., help="Text string to hash.")) :
    text_result = hash_text(text)  
    display_hash_table(text_result) 

@app.command(help="Generate cryptographic hashes for the specified file.")
def file(path: str = typer.Argument(..., help="Path to the input file.")) :
    try : 
        file_result = hash_file(path) 
        display_hash_table(file_result) 

    except FileNotFoundError :
        typer.secho(f"Error: File '{path}' not found.", fg=typer.colors.RED)

    except IsADirectoryError :
        typer.secho(f"Error: '{path}' is a directory, not a file.", fg=typer.colors.RED)
        
    except PermissionError :
        typer.secho(f"Error: Permission denied while accessing '{path}'.", fg=typer.colors.RED) 

@app.command(name = "verify-text", help="Verify a text string against a user-provided hash.") 
def verify_text(text:str = typer.Argument(..., help="Text string to verify."), target_hash:str = typer.Argument(..., help="Hash value used for verification.")) :
    try :
        text_hash_result = hash_text(text) 
        verification_result = verify_hash(text_hash_result, target_hash) 
        display_verification_result(verification_result) 
    
    except FileNotFoundError :
        typer.secho(f"Error: File '{path}' not found.", fg=typer.colors.RED)

    except IsADirectoryError :
        typer.secho(f"Error: '{path}' is a directory, not a file.", fg=typer.colors.RED)
        
    except PermissionError :
        typer.secho(f"Error: Permission denied while accessing '{path}'.", fg=typer.colors.RED) 

@app.command(name = "verify-file", help="Verify a file against a user-provided hash.") 
def verify_file(path: str = typer.Argument(..., help="Path to the input file."), target_hash: str = typer.Argument(..., help="Hash value used for verification.")) :
    try : 
        file_hash_result = hash_file(path)   
        verification_result = verify_hash(file_hash_result, target_hash) 
        display_verification_result(verification_result) 

    except FileNotFoundError :
        typer.secho(f"Error: File '{path}' not found.", fg=typer.colors.RED)

    except IsADirectoryError :
        typer.secho(f"Error: '{path}' is a directory, not a file.", fg=typer.colors.RED)
        
    except PermissionError :
        typer.secho(f"Error: Permission denied while accessing '{path}'.", fg=typer.colors.RED) 
        
