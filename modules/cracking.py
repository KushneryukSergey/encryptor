from modules import frequencies, cyphers
from modules.alphabet import Alphabet
import math


def _break_caesar_cypher(text: str, lang: str, freq_path='frequencies_data.json') -> str:
    frequencies.check(lang, freq_path)
    best_shift = 0
    bias = math.inf
    standard_freq = frequencies.get_saved_freq(freq_path)
    freq = frequencies.count_frequencies(text, lang)
    for shift in range(Alphabet.size()):
        new_freq = frequencies.shift_freq(freq, shift)
        new_bias = frequencies.count_bias(new_freq, standard_freq)
        if new_bias < bias:
            bias = new_bias
            best_shift = shift
    return cyphers.encode('caesar', text, best_shift, lang)


def _break_vigenere_cypher(text: str, lang: str) -> str:
    raise NotImplementedError('Not available now')


def break_cypher(cypher: str, text: str, lang: str, freq_path: str) -> str:
    if cypher == 'caesar':
        return _break_caesar_cypher(text, lang, freq_path)
    elif cypher == 'vigenere':
        return _break_vigenere_cypher(text, lang)
    elif cypher == 'vernam':
        raise TypeError("It's impossible to crack Vernam cypher\n \
                https://en.wikipedia.org/wiki/One-time_pad#Perfect_secrecy")
    else:
        raise TypeError('Incorrect cypher')
