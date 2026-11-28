"""Count the words in a text file: words are separated by any whitespace."""


def count_words(path):
    # utf-8-sig also accepts files saved with a byte-order mark (common on Windows).
    with open(path, encoding="utf-8-sig") as fh:
        return len(fh.read().split())
