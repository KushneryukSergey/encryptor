from modules.alphabet import Alphabet
import operator


def _encode_caesar(text: str, key, lang: str):
    try:
        key = int(key)
    except ValueError:
        raise TypeError("Invalid key for caesar cypher\n")
    result = []
    for letter in text:
        pos = Alphabet.get_pos_by(letter)
        if pos is not None:
            result.append(Alphabet.get_letter_by(pos + key))
        else:
            result.append(letter)
    return "".join(result)


def _decode_caesar(text: str, key, lang: str):
    try:
        key = int(key)
    except ValueError:
        raise TypeError("Invalid key for caesar cypher\n")
    return _encode_caesar(text, -key, lang)


def transform(text: str, key, lang: str, is_encode: bool, vernam=False):
    if is_encode:
        ops = operator.add
    else:
        ops = operator.sub
    index = 0
    result = []
    for letter in text:
        pos = Alphabet.get_pos_by(letter)
        if pos is not None:
            result.append(Alphabet.get_letter_by(ops(pos, Alphabet.get_pos_by(key[index]))))
        else:
            result.append(letter)
        index += 1
        if not vernam and index == len(key):
            index = 0
        return "".join(result)


def _encode_vigenere(text: str, key, lang: str):
    return transform(text, key, lang, is_encode=True)


def _decode_vigenere(text: str, key, lang: str):
    return transform(text, key, lang, is_encode=True)


def _encode_vernam(text: str, key, lang: str):
    if len(text) > len(key):
        raise TypeError("Incorrect key for Vernam cypher")
    return transform(text, key, lang, is_encode=True, vernam=True)


def _decode_vernam(text: str, key, lang: str):
    if len(text) > len(key):
        raise TypeError("Incorrect key for Vernam cypher")
    return transform(text, key, lang, is_encode=False, vernam=True)


def encode(cypher: str, text: str, key, lang: str):
    if cypher == "caesar":
        return _encode_caesar(text, key, lang)
    elif cypher == "vigenere":
        return _encode_vigenere(text, key, lang)
    elif cypher == "vernam":
        with open(key, "r") as key_file:
            return _encode_vernam(text, key_file.read(), lang)
    else:
        raise TypeError("Incorrect cypher")


def decode(cypher: str, text: str, key, lang: str):
    if cypher == "caesar":
        return _decode_caesar(text, key, lang)
    elif cypher == "vigenere":
        return _decode_vigenere(text, key, lang)
    elif cypher == "vernam":
        with open(key, "r") as key_file:
            return _decode_vernam(text, key_file.read(), lang)
    else:
        raise TypeError("Incorrect cypher")
