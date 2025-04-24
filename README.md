# Bfthon 🧠⇄🐍

![GitHub forks](https://img.shields.io/github/forks/whotfusests/bfthon?style=social)
![GitHub stars](https://img.shields.io/github/stars/whotfusests/bfthon?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/whotfusests/bfthon?style=social)
![GitHub Release](https://img.shields.io/github/v/release/whotfusests/bfthon?&logo=github&logoColor=white)
![Version](https://img.shields.io/badge/Version-1.0.0-233572A5?&logo=github&logoColor=white)
[![Made with](https://img.shields.io/badge/language-Python-%233572A5?logo=python&logoColor=white)](https://www.python.org/)

A lightweight Python module for bidirectional conversion between Python strings and Brainfuck code.

## Features

- 🔄 **Bi-directional Conversion**
  - Encode Python strings → Brainfuck
  - Decode Brainfuck → Python strings
- 🚀 **Zero Dependencies** - Pure Python implementation.
- 🐍 **Python 3.6+ Compatible**
- 📦 **Lightweight** - Single file module. 

## Installation

```bash
pip install https://github.com/whotfusests/bfthon.git
```

## Usage Examples

### Basic Encoding

```python
from bfthon import encode

# Convert Python to Brainfuck
bf_code = bfthon.encode('print("Hello World")')
print(bf_code)
# Output: ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++.++.---------.+++++.++++++.<<++++++++++.------.>++.>---------------.+++++++..+++.<<--.>+++++++++++++++.>.+++.------.--------.<<++.+++++++
```

### Basic Decoding

```python
from bfthon import decode

# Convert Brainfuck to Python
output = bfthon.decode("++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++++.++.---------.+++++.++++++.<<++++++++++.------.>++.>---------------.+++++++..+++.<<--.>+++++++++++++++.>.+++.------.--------.<<++.+++++++")
print(output)
# Output: Hello World
```

### Advanced Usage

```python
import bfthon

# Chain operations
message = "Secret Message"
bf_encoded = bfthon.encode(message)
decoded = bfthon.decode(bf_encoded)
assert message == decoded  # True
```

## API Reference

### `encode(s: str) -> str`
Converts a Python string to Brainfuck code that outputs the original string when executed.

**Parameters:**
- `s`: Input string to encode

**Returns:**
- Brainfuck code as a string

### `decode(bf_code: str) -> str`
Executes Brainfuck code and returns the output as a Python string.

**Parameters:**
- `bf_code`: Valid Brainfuck code to decode

**Returns:**
- Decoded Python string

## License
This repository/module uses MIT Open Source License.

**© 2025 [whotfusests](https://github.com/whotfusests)**
