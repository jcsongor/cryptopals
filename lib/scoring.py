from abc import ABC
from sortedcontainers import SortedDict


class ScoringStrategy(ABC):
    def score(self, plaintext: str):
        raise NotImplementedError()


class WordScoringStrategy(ScoringStrategy):
    def __init__(self, word_list_file: str):
        with open(word_list_file) as words:
            self._words = [line.lower().strip() for line in words]

    def _possible_words(self, sentence: str) -> list:
        return [sentence[word_start:word_end].lower() for word_start in range(len(sentence) - 1) for word_end in
                range(word_start, len(sentence))]

    def _is_valid_word(self, word: str) -> bool:
        return word in self._words


class WordLengthScoringStrategy(WordScoringStrategy):
    def score(self, sentence: str) -> int:
        words = self._possible_words(sentence)
        return sum([len(word) for word in words if self._is_valid_word(word)])


class WordCountScoringStrategy(WordScoringStrategy):
    def score(self, sentence: str) -> int:
        words = self._possible_words(sentence)
        return len([word for word in words if self._is_valid_word(word)])


class LetterFrequencyScoringStrategy(ScoringStrategy):
    def __init__(self, letter_list_file: str):
        with open(letter_list_file) as lines:
            self._letters = dict((self._parse_letter_list_line(line) for line in lines))

    def score(self, text: str) -> int:
        frequencies = self._letter_frequencies(text)
        return -sum([self._deviation(*frequency) for frequency in frequencies.items()])

    def _parse_letter_list_line(self, line: str) -> tuple:
        letter, frequency = line.lower().strip().split(',')
        return letter, float(frequency)

    def _letter_frequencies(self, text: str) -> dict:
        text_length = float(len(text))
        return {char.lower(): text.count(char) / text_length for char in set(text)}

    def _deviation(self, letter: str, frequency: float):
        return abs(frequency - self._letters.get(letter, 1))


class PlainTextGuesser:
    def __init__(self, scoring_strategy: ScoringStrategy):
        self._scoring_strategy = scoring_strategy

    def most_likely_plaintext(self, candidates: list) -> str:
        scored_plaintexts = SortedDict((self._scored_plaintext(candidate) for candidate in candidates))

        return self._get_candidate_with_highest_score(scored_plaintexts)

    def _scored_plaintext(self, plaintext: str) -> tuple:
        return (self._scoring_strategy.score(plaintext), plaintext)

    def _get_candidate_with_highest_score(self, ordered_plaintexts: SortedDict) -> str:
        _, message = ordered_plaintexts.peekitem()

        return message
