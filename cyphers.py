import alphabet
import operator


def encode_caesar(text: str, key: int, lang: str):
    alphabet.define_alphabet(lang)
    base = len(alphabet.ALPHABET)
    pos = alphabet.alphabet_positions()
    result = ""
    for i in text:
        if i in alphabet.ALPHABET:
            result += alphabet.ALPHABET[(pos[i] + key) % base]
        else:
            result += i
    return result


def decode_caesar(text: str, key: int, lang: str):
    return encode_caesar(text, -key, lang)


def encode_vv(text: str, key: str, lang: str, action: str, vernam=False):
    ops = {"+": operator.add,
           "-": operator.sub}
    alphabet.define_alphabet(lang)
    base = len(alphabet.ALPHABET)
    pos = alphabet.alphabet_positions()
    index = 0
    result = ""
    for i in text:
        if i in alphabet.ALPHABET:
            result += alphabet.ALPHABET[ops[action](pos[i], pos[key[index]]) % base]
        else:
            result += i
        index += 1
        if not vernam and index == len(key):
            index = 0
    return result


def encode_vigenere(text: str, key: str, lang: str):
    return encode_vv(text, key, lang, "+")


def decode_vigenere(text: str, key: str, lang: str):
    return encode_vv(text, key, lang, "-")


def encode_vernam(text: str, key: str, lang: str):
    if len(text) > len(key):
        raise TypeError("Incorrect key for Vernam cypher")
    return encode_vv(text, key, lang, "+", True)


def decode_vernam(text: str, key: str, lang: str):
    if len(text) > len(key):
        raise TypeError("Incorrect key for Vernam cypher")
    return encode_vv(text, key, lang, "-", True)


def encode(cypher: str, text: str, key, lang: str):
    if cypher == "caesar":
        return encode_caesar(text, key, lang)
    elif cypher == "vigenere":
        return encode_vigenere(text, key, lang)
    elif cypher == "vernam":
        return encode_vernam(text, key, lang)
    else:
        raise TypeError("Incorrect cypher")


def decode(cypher: str, text: str, key, lang: str):
    if cypher == "caesar":
        return decode_caesar(text, key, lang)
    elif cypher == "vigenere":
        return decode_vigenere(text, key, lang)
    elif cypher == "vernam":
        return decode_vernam(text, key, lang)
    else:
        raise TypeError("Incorrect cypher")
