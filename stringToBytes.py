def stringToBytes(src):
    bytes = []
    for character in src:
        bytes.append(ord(character))
    return bytes