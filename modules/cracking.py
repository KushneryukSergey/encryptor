from modules import alphabet, frequencies, cyphers


def crack_caesar(text: str, lang: str, freq_file="frequencies_data.json") -> str:
    alphabet.define_alphabet(lang)
    frequencies.check(lang, freq_file)
    base = len(alphabet.ALPHABET)
    pos = alphabet.alphabet_positions()
    best_result = text
    bias = frequencies.bias(text, lang)
    for i in range(1, base):
        result = cyphers.encode_caesar(text, i, lang)
        new_bias = frequencies.bias(result, lang)
        if new_bias < bias:
            bias = new_bias
            best_result = result
    return best_result


def crack_vigenere(text: str, lang: str) -> str:
    raise TypeError("Not available now")


def crack(cypher: str, text: str, lang: str, freq_path: str) -> str:
    if cypher == "caesar":
        return crack_caesar(text, lang, freq_path)
    elif cypher == "vigenere":
        return crack_vigenere(text, lang)
    elif cypher == "vernam":
        raise TypeError("It's impossible to crack Vernam cypher\n \
                https://en.wikipedia.org/wiki/One-time_pad#Perfect_secrecy")
    else:
        raise TypeError("Incorrect cypher")
