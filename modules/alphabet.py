import string


ALPHABET = ""
_ALPHABET_DEFINED = False
ENGLISH = "en"
RUSSIAN = "ru"


def russian_lowercase_alphabet() -> str:
    return "".join(["%c" % (i + 1072 - (i > 6)) if i != 6 else "ё" for i in range(0, 32)])


def russian_uppercase_alphabet() -> str:
    return russian_lowercase_alphabet().upper()


def mixed_russian_alphabet() -> str:
    return "".join([upper_letter+lower_letter for upper_letter, lower_letter in
                    zip(russian_uppercase_alphabet(), russian_lowercase_alphabet())])


def russian_alphabet() -> str:
    return russian_uppercase_alphabet() + russian_lowercase_alphabet()


def english_lowercase_alphabet() -> str:
    return string.ascii_lowercase


def english_uppercase_alphabet() -> str:
    return string.ascii_uppercase


def mixed_english_alphabet() -> str:
    return "".join([upper_letter+lower_letter for upper_letter, lower_letter in
                    zip(english_uppercase_alphabet(), english_lowercase_alphabet())])


def english_alphabet() -> str:
    return english_uppercase_alphabet() + english_lowercase_alphabet()


def define_alphabet(language: str):
    global _ALPHABET_DEFINED
    if _ALPHABET_DEFINED:
        return
    global ALPHABET
    if language == ENGLISH:
        ALPHABET = english_alphabet()
    elif language == RUSSIAN:
        ALPHABET = russian_alphabet()
    else:
        raise TypeError("Incorrect language")
    ALPHABET += string.digits + string.punctuation
    _ALPHABET_DEFINED = True


def alphabet_positions() -> dict:
    return {ALPHABET[i]: i for i in range(len(ALPHABET))}


if __name__ == "__main__":
    print(russian_alphabet())
    print(english_alphabet())
    define_alphabet(ENGLISH)
    print(ALPHABET)
