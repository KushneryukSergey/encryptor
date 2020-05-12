import json
import os
from modules.alphabet import Alphabet


def count_frequencies(text: str, lang: str) -> dict:
    count = dict.fromkeys(range(Alphabet.size()), 0)
    counter = 0
    result = []
    for letter in text:
        pos = Alphabet.get_pos_by(letter)
        if pos is not None:
            count[pos] += 1
            counter += 1
    return {Alphabet.get_letter_by(pos): frequency / counter for pos, frequency in count.items()}


def shift_freq(frequencies: dict, shift: int) -> dict:
    result = dict()
    for letter, frequency in frequencies.items():
        result[Alphabet.get_letter_by(Alphabet.get_pos_by(letter) + shift)] = frequency
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


def get_saved_freq(freq_path: str):
    with open(freq_path, "r") as read_file:
        return json.load(read_file)


if __name__ == "__main__":
    Alphabet.make_alphabet("en")
    with open("../texts/The_Breathing_Method-Stephen_King.txt", "r") as file:
        book = file.read()
    save_frequencies(book, "en", "../devs/freq.json")
    print(get_saved_freq("../devs/freq.json"))
