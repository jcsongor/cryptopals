def sxorc(string: str, char: int) -> str:
    return ''.join([chr(int(c1) ^ char) for c1 in string])


def sxors(string1: str, string2: str) -> str:
    return '%x' % (int(string1, 16) ^ int(string2, 16))

def sxorc_with_every_possible_key(ciphertext: str) -> list:
    alpha = list(range(ord('a'), ord('z')))
    num = list(range(ord('0'), ord('9')))
    return [sxorc(ciphertext, key) for key in alpha + num]
