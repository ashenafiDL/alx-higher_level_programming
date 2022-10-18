#!/usr/bin/python3
"""Defins a function that prints a text with 2 new lines
after each of these characters: `.`, `?` and `:`
"""


def text_indentation(text) -> None:
    """prints a text with 2 new lines
    after each of these characters: `.`, `?` and `:`

    Args:
        text (str): the input string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ['.', '?', ':']:
            print(text[i] + "\n")
            if i < len(text) - 1 and text[i+1] == ' ':
                i += 1
        else:
            print(text[i], end="")

        i += 1
