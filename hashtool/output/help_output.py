import typer

def print_help() :
    typer.echo("""
    HashTool 1.0.0
    Copyright (c) 2026 Hafeez Choudhary
    
    Usage:
        hashtool [OPTIONS]

    Description:
        Generate, verify, and inspect cryptographic hashes for text and files.

    Options:
        -t, --text TEXT              Hash the provided text.
        -f, --file PATH              Hash the specified file.
        -v, --verify HASH            Verify generated hash against HASH.
        -a, --algorithm ALGORITHMS   Specify algorithm(s) (md5, sha1, sha256, sha512).
                                    Multiple values: md5,sha256
        -d, --detect HASH            Detect possible algorithm(s) from a hash.
        -h, --help                   Show this help message and exit.

    Examples:

        Hash text
            hashtool -t "hello"

        Hash file
            hashtool -f sample.txt

        Hash using specific algorithm
            hashtool -t "hello" -a sha256

        Hash using multiple algorithms
            hashtool -t "hello" -a md5,sha256

        Verify text
            hashtool -t "hello" --verify 5d41402abc4b2a76b9719d911017c592

        Verify file
            hashtool -f sample.txt --verify <HASH>

        Verify using specific algorithm
            hashtool -t "hello" --verify <HASH> -a sha256

        Detect hash algorithm
            hashtool --detect 5d41402abc4b2a76b9719d911017c592
        """)