import typer

def print_help() :
    typer.echo("""
    HashCLI 1.0.0
    Copyright (c) 2026 Hafeez Choudhary
    
    Usage:
        hashcli [OPTIONS]

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
            hashcli -t "hello"

        Hash file
            hashcli -f sample.txt

        Hash using specific algorithm
            hashcli -t "hello" -a sha256

        Hash using multiple algorithms
            hashcli -t "hello" -a md5,sha256

        Verify text
            hashcli -t "hello" --verify 5d41402abc4b2a76b9719d911017c592

        Verify file
            hashcli -f sample.txt --verify <HASH>

        Verify using specific algorithm
            hashcli -t "hello" --verify <HASH> -a sha256

        Detect hash algorithm
            hashcli --detect 5d41402abc4b2a76b9719d911017c592
        """)