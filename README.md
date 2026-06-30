# HashTool

A lightweight command-line utility for generating, verifying, and detecting cryptographic hashes for text and files.

## Features

- Generate MD5, SHA-1, SHA-256, and SHA-512 hashes
- Hash text input
- Hash files
- Verify hashes
- Detect possible hash algorithms
- Select one or multiple hashing algorithms
- Rich terminal output
- Built with Typer

## Installation

```bash
pip install hashtool
```

## Usage

### Hash text

```bash
hashtool -t "Hello"
```

### Hash file

```bash
hashtool -f sample.txt
```

### Hash using a specific algorithm

```bash
hashtool -t "Hello" -a sha256
```

### Hash using multiple algorithms

```bash
hashtool -t "Hello" -a md5,sha256
```

### Verify a hash

```bash
hashtool -t "Hello" --verify 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

### Detect possible algorithm

```bash
hashtool --detect 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

## Supported Algorithms

- MD5
- SHA-1
- SHA-256
- SHA-512

> **Note:** MD5 and SHA-1 are supported for compatibility and educational purposes. For modern security applications, use SHA-256 or SHA-512 instead.

## Technologies

- Python
- Typer
- Rich
- hashlib

## License

MIT License