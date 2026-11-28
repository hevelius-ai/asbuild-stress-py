"""Count the words in a text file."""


def count_words(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    # Every word is followed by a space or a line break, so counting those
    # separators counts the words without building a list of them.
    return text.count(" ") + text.count("\n")
