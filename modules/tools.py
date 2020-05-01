from sys import stdin


def input_text(file: str):
    if file == "CONSOLE":
        text = ""
        for line in stdin:
            text += line
    else:
        f = open(file, "r")
        text = f.read()
        f.close()
    return text


def output_text(file: str, text: str):
    if file == "CONSOLE":
        print(text)
    else:
        f = open(file, "w")
        f.write(text)
        f.close()
