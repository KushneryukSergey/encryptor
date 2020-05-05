from sys import stdin
from string import whitespace


CONSOLE = "console"


def input_text(file: str):
    if file == CONSOLE:
        text = "".join(stdin)
        while text[-1] in whitespace:
            text = text[0:-1]
    else:
        f = open(file, "r")
        text = f.read()
        f.close()
    return text


def output_text(file: str, text: str):
    if file == CONSOLE:
        print(text)
    else:
        f = open(file, "w")
        f.write(text)
        f.close()
