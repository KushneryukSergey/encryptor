import string


ALPHABET = ""
__ALPHABET_DEFINED = False


def russian_lowercase_alphabet() -> str:
    return "".join(["%c" % (i + 1072 - (i > 6)) if i != 6 else "ё" for i in range(0, 32)])


def russian_uppercase_alphabet() -> str:
    return russian_lowercase_alphabet().upper()


def russian_alphabet() -> str:
    return "".join([upper_letter+lower_letter for upper_letter, lower_letter in
                    zip(russian_uppercase_alphabet(), russian_lowercase_alphabet())])


def english_lowercase_alphabet() -> str:
    return string.ascii_lowercase


def english_uppercase_alphabet() -> str:
    return string.ascii_uppercase


def english_alphabet() -> str:
    return "".join([upper_letter+lower_letter for upper_letter, lower_letter in
                    zip(english_uppercase_alphabet(), english_lowercase_alphabet())])


def define_alphabet(language: str):
    global __ALPHABET_DEFINED
    if __ALPHABET_DEFINED:
        return
    global ALPHABET
    if language == "en":
        ALPHABET = english_alphabet()
    elif language == "ru":
        ALPHABET = russian_alphabet()
    else:
        raise TypeError("Incorrect language")
    ALPHABET += string.digits + string.punctuation
    __ALPHABET_DEFINED = True


def alphabet_positions() -> dict:
    return {ALPHABET[i]: i for i in range(len(ALPHABET))}


if __name__ == "__main__":
    print(russian_alphabet())
    print(english_alphabet())
    define_alphabet("en")
    print(ALPHABET)
