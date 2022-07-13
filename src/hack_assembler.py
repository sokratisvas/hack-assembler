SYMBOLS = {
    "SCREEN": 16384, "KBD": 24576, "SP": 0, 
    "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4 
}

for i in range(16): 
    SYMBOLS['R' + str(i)] = i

def parser(filename, SYMBOLS):
    # Get tokens and add label symbols to symbols
    filepath = "../hack-examples/" + filename
    with open(filepath, mode = 'r', encoding = "utf-8") as f:
        tokens = [line.strip() for line in f if line.strip()[:2] != "//" and line.strip()]
        labels = [token for token in tokens if token.startswith('(') and token.endswith(')')]
    for label in labels:
        SYMBOLS[label[1:-1]] = tokens.index(label) - labels.index(label) 
    for label in labels:
        tokens.remove(label)
    
    for i in range(len(tokens)):
        print(f"{i}: {tokens[i]}")

    # Add variable symbols to symbols
    mem_address = 16
    for token in tokens:
        if token.startswith('@') and not token[1:].isdigit():
            if token[1:] not in SYMBOLS:
                SYMBOLS[token[1:]] = mem_address
                mem_address += 1

    # Generate binary
    executable = []



parser("mult.asm", SYMBOLS)
for symbol, address in SYMBOLS.items():
    print(f"{symbol}: {address}")

"""
tokens = parser("max.asm", SYMBOLS)
for token in tokens:
    print(token)

print("===========================")

tokens = parser("fill.asm", SYMBOLS)
for token in tokens:
    print(token)

print("===========================")

tokens = parser("mult.asm", SYMBOLS)
for token in tokens:
    print(token)
"""













