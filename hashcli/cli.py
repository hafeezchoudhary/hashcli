from hashcli.core.hash_text import hash_text 
from hashcli.output.console_output import display_hash_table 
from hashcli.core.hash_file import hash_file
from hashcli.core.verify_hash import verify_hash
from hashcli.output.verification_output import display_verification_result
from hashcli.core.detect_algorithm import detect_algorithm
from hashcli.output.detect_output import display_detect_result
from hashcli.output.help_output import print_help
import typer 

app = typer.Typer(help="HashCLI - Command-line utility for generating and verifying cryptographic hashes.")

@app.callback(invoke_without_command=True)
def main(
    text: str = typer.Option(
        None,
        "--text",
        "-t",
        help="Text string to hash.",
    ),
    path: str = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to the input file.",
    ),
    verify: str = typer.Option(
        None,
        "--verify",
        "-v",
        help="Verify a generated hash.",
    ),
    algorithm: str = typer.Option(
        None,
        "--algorithm",
        "-a",
        help="Hash algorithm(s) to use."
    ), 
    detect: str = typer.Option(
        None,
        "--detect",
        "-d",
        help="Detect algorithm(s)."
    ),
    help_option: bool = typer.Option(
        False,
        "--help",
        "-h",
        help="Show help message and exit.",
    )
) :

    if help_option:
        print_help()
        raise typer.Exit()

    # ---------------- Validation ---------------- #

    if text and path:
        typer.secho("Error: Use either --text (-t) or --file (-f), not both.", fg=typer.colors.RED)
        raise typer.Exit(code=1)
    if detect and (text or path) :
        typer.secho("Error: --detect (-d) cannot be used with --text (-t) or --file (-f).", fg=typer.colors.RED)
        raise typer.Exit(code=1) 

    if not text and not path and not detect:
        typer.secho("Error: Please provide either --text (-t), --file (-f) or --detect (-d).", fg=typer.colors.RED)
        raise typer.Exit(code=1)

    # ---------------- TEXT ---------------- #


    selected_algorithms = (
        [alg.strip().lower() for alg in algorithm.split(",")]
        if algorithm
        else None
    )

    SUPPORTED_ALGORITHMS = {
        "md5",
        "sha1",
        "sha256",
        "sha512",
    }

    if selected_algorithms:
        for alg in selected_algorithms:
            if alg not in SUPPORTED_ALGORITHMS:
                typer.secho(f"Error: Unsupported algorithm '{alg}'.", fg=typer.colors.RED)
                typer.echo("Supported algorithms: md5, sha1, sha256, sha512")
                raise typer.Exit(code=1)

    if text:
        text_result = hash_text(text, selected_algorithms)

        if verify:
            verification_result = verify_hash(text_result, verify)
            display_verification_result(verification_result)

        else:
            display_hash_table(text_result)

    # ---------------- FILE ---------------- #

    elif path:
        try:
            file_result = hash_file(path, selected_algorithms)

            if verify:
                verification_result = verify_hash(file_result, verify)
                display_verification_result(verification_result)

            else:
                display_hash_table(file_result)

        except FileNotFoundError:
            typer.secho(f"Error: File '{path}' not found.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        except IsADirectoryError:
            typer.secho(f"Error: '{path}' is a directory, not a file.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

        except PermissionError:
            typer.secho(f"Error: Permission denied while accessing '{path}'.", fg=typer.colors.RED)
            raise typer.Exit(code=1)

    #------------------Detect algorithm------------------
    if detect :
        detect_result = detect_algorithm(detect)
        display_detect_result(detect_result)
