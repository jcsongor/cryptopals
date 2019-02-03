
def sxorc(string: str, char: int) -> str:
    return ''.join([chr(int(c1) ^ char) for c1 in string])


def sxors(string1: str, string2: str) -> str:
    return '%x' % (int(string1, 16) ^ int(string2, 16))
