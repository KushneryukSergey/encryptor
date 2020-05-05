import json
import os
from modules import alphabet

FREQ_PATH = ""


def __count_freq__(text: str, lang: str):
    alphabet.define_alphabet(lang)
    count = {i: 0 for i in alphabet.ALPHABET}
    counter = 0
    for letter in text:
        if letter in alphabet.ALPHABET:
            count[letter] += 1
            counter += 1
    return {i: count[i]/counter for i in alphabet.ALPHABET}


def count_frequencies(text: str, lang: str, freq_path: str):
    global FREQ_PATH
    FREQ_PATH = freq_path
    with open(FREQ_PATH, "w") as freq_file:
        json.dump(__count_freq__(text, lang), freq_file)


def check(lang: str, freq_file):
    global FREQ_PATH
    FREQ_PATH = freq_file
    if not (os.path.isfile(FREQ_PATH) and os.path.getsize(FREQ_PATH) > 0):
        raise TypeError("There is no frequencies to crack caesar cypher")


def bias(text: str, lang: str) -> float:
    result = 0.0
    text_freq = __count_freq__(text, lang)
    standard_freq = __saved_freq__()
    for letter in alphabet.ALPHABET:
        result += (text_freq.get(letter, 0) - standard_freq.get(letter, 0))**2
    return result


def __saved_freq__():
    with open(FREQ_PATH, "r") as read_file:
        return json.load(read_file)


if __name__ == "__main__":
    with open("../texts/The_Breathing_Method-Stephen_King.txt", "r") as f:
        book = "".join(f.read())
    count_frequencies(book, "en", "../devs/freq.json")
    print(__saved_freq__())
