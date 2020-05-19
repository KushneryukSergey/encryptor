import json
import os
from modules.alphabet import Alphabet


def count_frequencies(text: str, lang: str) -> dict:
    count = dict.fromkeys(Alphabet.current_alphabet, 0)
    counter = 0
    result = []
    for letter in text:
        if Alphabet.contains(letter):
            count[letter] += 1
            counter += 1
    for letter in count.keys():
        count[letter] /= counter
    return count


def shift_freq(frequencies: dict, shift: int) -> dict:
    result = dict()
    for letter, frequency in frequencies.items():
        result[Alphabet.shift_letter_by(letter, shift)] = frequency
    return result


def save_frequencies(text: str, lang: str, freq_path: str):
    with open(freq_path, "w") as freq_file:
        json.dump(count_frequencies(text, lang), freq_file)


def check(lang: str, freq_path: str):
    if not (os.path.isfile(freq_path) and os.path.getsize(freq_path) > 0):
        raise TypeError("There is no frequencies to crack caesar cypher")


def count_bias(first_freq: dict, second_freq: dict) -> float:
    result = 0.0
    for letter in first_freq.keys():
        result += (first_freq.get(letter, 0) - second_freq.get(letter, 0))**2
    return result
