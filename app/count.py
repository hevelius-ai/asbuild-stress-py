"""Count the words in a text file: a word is any run of characters that are not whitespace."""

import re

_WORD = re.compile(r"\S+")


def count_words(path):
    with open(path, encoding="utf-8") as fh:
        return sum(1 for _ in _WORD.finditer(fh.read()))
