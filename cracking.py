import alphabet
import freq
import cyphers


def crack_caesar(text: str, lang: str) -> str:
    alphabet.define_alphabet(lang)
    freq.check(lang)
    base = len(alphabet.ALPHABET)
    pos = alphabet.alphabet_positions()
    best_result = text
    bias = freq.bias(text, lang)
    for i in range(1, base):
        result = cyphers.encode_caesar(text, i, lang)
        new_bias = freq.bias(result, lang)
        if new_bias < bias:
            bias = new_bias
            best_result = result
    return best_result


def crack_vigenere(text: str, lang: str) -> str:
    return "cannot do it now"


def crack(cypher: str, text: str, lang: str) -> str:
    if cypher == "caesar":
        return crack_caesar(text, lang)
    elif cypher == "vigenere":
        return crack_vigenere(text, lang)
    elif cypher == "vernam":
        return "It's impossible to crack Vernam cypher"
    else:
        raise TypeError("Incorrect cypher")