from sys import stdin
from string import whitespace


CONSOLE = None


def read_text(file):
    if file is CONSOLE:
        text = stdin.read()
        text = text.rstrip(whitespace)
    else:
        with open(file, "r") as read_file:
            text = read_file.read()
    return text


def print_text(file, text: str):
    if file is CONSOLE:
        print(text)
    else:
        with open(file, "w") as read_file:
            read_file.write(text)


if __name__ == "__main__":
    print(whitespace)
