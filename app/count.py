"""Count the words in a text file: words are separated by any whitespace.

The file is read in chunks so a very large file does not have to fit in memory.
"""

CHUNK = 64 * 1024


def count_words(path):
    words = 0
    carry = ""
    with open(path, encoding="utf-8") as fh:
        while True:
            chunk = fh.read(CHUNK)
            if chunk is None:  # end of file
                break
            text = carry + chunk
            parts = text.split()
            # A word cut in half at the chunk edge is carried into the next chunk.
            if parts and text and not text[-1].isspace():
                carry = parts.pop()
            else:
                carry = ""
            words += len(parts)
    if carry:
        words += 1
    return words
