from collections import defaultdict

def encode(s: str) -> str:
    bf_code = []
    for i, char in enumerate(s):
        c = ord(char)
        if i == 0:
            part = '+' * c
        else:
            part = '[-]' + '+' * c
        bf_code.append(part)
        bf_code.append('.')
    return ''.join(bf_code)

def decode(bf_code: str) -> str:
    bracket_map = {}
    stack = []
    for i, c in enumerate(bf_code):
        if c == '[':
            stack.append(i)
        elif c == ']':
            if not stack:
                raise ValueError(f"Unmatched ']' at position {i}")
            start = stack.pop()
            bracket_map[start] = i
            bracket_map[i] = start
    if stack:
        raise ValueError(f"Unmatched '[' at positions {stack}")
    
    data = defaultdict(int)
    pointer = 0
    output = []
    code_ptr = 0
    
    while code_ptr < len(bf_code):
        cmd = bf_code[code_ptr]
        if cmd == '>':
            pointer += 1
        elif cmd == '<':
            pointer -= 1
        elif cmd == '+':
            data[pointer] = (data[pointer] + 1) % 256
        elif cmd == '-':
            data[pointer] = (data[pointer] - 1) % 256
        elif cmd == '.':
            output.append(chr(data[pointer]))
        elif cmd == ',':
            data[pointer] = 0
        elif cmd == '[':
            if data[pointer] == 0:
                code_ptr = bracket_map[code_ptr]
        elif cmd == ']':
            if data[pointer] != 0:
                code_ptr = bracket_map[code_ptr]
        code_ptr += 1
    
    return ''.join(output)