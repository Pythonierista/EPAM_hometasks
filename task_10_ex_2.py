"""Implement a function `most_common_words(file_path: str, top_words: int) -> list`
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned

Example:

print(most_common_words(file_path, 3))
>>> ['donec', 'etiam', 'aliquam']
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re


def most_common_words(text, top_words):
    d = {}
    l = re.findall('[a-zA-Z]+', ''.join([i.lower() for i in open(text)]))
    for i in l:
        d[i] = d.get(i, 0) + 1
    result = sorted([i for i in d.items()], key=lambda x: x[1], reverse=True)[:top_words]
    return [i[0] for i in result]
