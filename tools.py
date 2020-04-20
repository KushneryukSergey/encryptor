def input_text(file: str):
    f = open(file, "r")
    text = f.read()
    f.close()
    return text


def output_text(file: str, text: str):
    f = open(file, "w")
    f.write(text)
    f.close()