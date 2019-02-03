#!/usr/bin/env python3

from binascii import unhexlify
from lib.xor import sxorc
from lib.scoring import \
    LetterFrequencyScoringStrategy, \
    PlainTextGuesser, \
    WordCountScoringStrategy, \
    WordLengthScoringStrategy
from lib.timer import timer


def decipher_with_every_key(ciphertext: str) -> dict:
    return {chr(key): sxorc(ciphertext, key) for key in range(ord('a'), ord('z'))}


def guess_plaintext(possible_plaintexts: dict, guesser: PlainTextGuesser) -> None:
    plaintext = guesser.most_likely_plaintext(possible_plaintexts)

    assert plaintext['key'] == 'x'
    assert plaintext['message'] == 'cOOKING\x00mc\x07S\x00LIKE\x00A\x00POUND\x00OF\x00BACON'


ciphertext = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

possible_plaintexts = decipher_with_every_key(ciphertext)

with timer('Letter frequency strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(LetterFrequencyScoringStrategy('letters.csv')))

with timer('Word length strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(WordLengthScoringStrategy('words.txt')))

with timer('Word count strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(WordCountScoringStrategy('words.txt')))
