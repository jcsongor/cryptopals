
def sxorc(string: str, char: str) -> bytes:
    return ''.join([chr(c1 ^ char) for c1 in string])


def sxors(string1: str, string2: str) -> bytes:
    return b'%x' % (int(string1, 16) ^ int(string2, 16))
