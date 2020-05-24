# -*- coding: utf-8 -*-
from modules.alphabet import Alphabet


def _encode_caesar(text: str, key, lang: str):
    try:
        key = int(key)
    except ValueError:
        raise TypeError('Invalid key for caesar cypher\n')
    result = []
    for letter in text:
        if Alphabet.contains(letter):
            result.append(Alphabet.shift_letter_by(letter, key))
        else:
            result.append(letter)
    return ''.join(result)


def _decode_caesar(text: str, key, lang: str):
    try:
        key = int(key)
    except ValueError:
        raise TypeError('Invalid key for caesar cypher\n')
    return _encode_caesar(text, -key, lang)


def _vigenere_transform(text: str, key, lang: str, is_encode: bool):
    if is_encode:
        sign = 1
    else:
        sign = -1
    shifts = [Alphabet.get_pos_by(letter) for letter in key]
    result = []
    for index, letter in enumerate(text):
        if Alphabet.contains(letter):
            result.append(Alphabet.shift_letter_by(letter, sign * shifts[index % len(key)]))
        else:
            result.append(letter)
    return ''.join(result)


def _vernam_transform(text: str, key, lang: str):
    result = []
    for letter, key_letter in zip(text, key):
        code = int.from_bytes(letter.encode('utf-32'), 'big') ^ int.from_bytes(key_letter.encode('utf-32'), 'big')
        result.append(code.to_bytes(4, 'big').decode('utf-32'))
    return ''.join(result)


def _encode_vigenere(text: str, key, lang: str):
    return _vigenere_transform(text, key, lang, is_encode=True)


def _decode_vigenere(text: str, key, lang: str):
    return _vigenere_transform(text, key, lang, is_encode=False)


def _encode_vernam(text: str, key, lang: str):
    if len(text) > len(key):
        raise TypeError('Incorrect key for Vernam cypher')
    return _vernam_transform(text, key, lang)


def _decode_vernam(text: str, key, lang: str):
    if len(text) > len(key):
        raise TypeError('Incorrect key for Vernam cypher')
    return _vernam_transform(text, key, lang)


def encode(cypher: str, text: str, key, lang: str):
    if cypher == 'caesar':
        return _encode_caesar(text, key, lang)
    elif cypher == 'vigenere':
        return _encode_vigenere(text, key, lang)
    elif cypher == 'vernam':
        with open(key, 'r') as key_file:
            return _encode_vernam(text, key_file.read(), lang)
    else:
        raise TypeError('Incorrect cypher')


def decode(cypher: str, text: str, key, lang: str):
    if cypher == 'caesar':
        return _decode_caesar(text, key, lang)
    elif cypher == 'vigenere':
        return _decode_vigenere(text, key, lang)
    elif cypher == 'vernam':
        with open(key, 'r') as key_file:
            return _decode_vernam(text, key_file.read(), lang)
    else:
        raise TypeError('Incorrect cypher')
