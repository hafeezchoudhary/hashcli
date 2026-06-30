# HashTool

A lightweight command-line utility for generating and verifying cryptographic hashes for text and files.
 
## Features

- Generate MD5, SHA-1, SHA-256 and SHA-512 hashes
- Hash text input
- Hash files
- Verify hashes
- Rich terminal output
- Built with Typer

## Installation

pip install hascli

## Usage

hascli text "Hello"

hascli file sample.txt

hascli verify-text "Hello" HASH

hascli verify-file sample.txt HASH

## Technologies

- Python
- Typer
- Rich
- hashlib

## License

MIT 