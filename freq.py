import json
import os
import alphabet
from tools import input_text, output_text


FREQ_PATH = "frequencies_data.json"


def __count_freq(text: str, lang: str):
    alphabet.define_alphabet(lang)
    result = {i: 0 for i in alphabet.ALPHABET}
    counter = 0
    for i in text:
        if i in alphabet.ALPHABET:
            result[i] += 1
            counter += 1
    for i in result.values():
        result[i] /= counter
    return result


def count_frequencies(text: str, lang: str):
    with open(FREQ_PATH, "w") as freq_file:
        json.dump(__count_freq(text, lang), freq_file)


def check(lang: str):
    if not (os.path.isfile(FREQ_PATH) and os.path.getsize(FREQ_PATH) > 0):
        raise TypeError("There is no frequencies to crack caesar cypher")


def bias(text: str, lang: str) -> float:
    result = 0.0
    for s, c in __stand_freq().values(), __count_freq(text, lang).values():
        result += (s - c)**2
    return result


def __stand_freq():
    with open(FREQ_PATH, "r") as read_file:
        return json.load(read_file)
