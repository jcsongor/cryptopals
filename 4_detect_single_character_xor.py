#!/usr/bin/env python3

from binascii import unhexlify
from lib.scoring import \
    LetterFrequencyScoringStrategy, \
    PlainTextGuesser
from lib.timer import timer
from lib.xor import sxorc_with_every_possible_key


def guess_plaintext(possible_plaintexts: list, guesser: PlainTextGuesser) -> None:
    plaintext = guesser.most_likely_plaintext(possible_plaintexts)

    assert plaintext == 'Now that the party is jumping\n'


with open('data/4.txt') as lines:
    ciphertexts = [unhexlify(line.strip()) for line in lines]

possible_plaintexts = []
for ciphertext in ciphertexts:
    possible_plaintexts += sxorc_with_every_possible_key(ciphertext)


with timer('Letter frequency strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(LetterFrequencyScoringStrategy('data/letters.csv')))
