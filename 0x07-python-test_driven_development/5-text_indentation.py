#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each (., ? & :).

    Args:
    text (str): The input txt.

    Raises:
    TypeError: If text is not a str.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = [".", "?", ":"]
    newText = ""

    for ch in text:
        newText += ch
        if ch in punctuation_marks:
            newText += "\n\n"

    print(newText.strip())
