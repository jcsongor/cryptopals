#!/usr/bin/env python3

from binascii import unhexlify
from lib.scoring import \
    LetterFrequencyScoringStrategy, \
    PlainTextGuesser, \
    WordCountScoringStrategy, \
    WordLengthScoringStrategy
from lib.timer import timer
from lib.xor import sxorc_with_every_possible_key


def guess_plaintext(possible_plaintexts: list, guesser: PlainTextGuesser) -> None:
    plaintext = guesser.most_likely_plaintext(possible_plaintexts)

    assert plaintext == 'cOOKING\x00mc\x07S\x00LIKE\x00A\x00POUND\x00OF\x00BACON'


ciphertext = unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

possible_plaintexts = sxorc_with_every_possible_key(ciphertext)

with timer('Letter frequency strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(LetterFrequencyScoringStrategy('data/letters.csv')))

with timer('Word length strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(WordLengthScoringStrategy('data/words.txt')))

with timer('Word count strategy'):
    guess_plaintext(possible_plaintexts, PlainTextGuesser(WordCountScoringStrategy('data/words.txt')))
