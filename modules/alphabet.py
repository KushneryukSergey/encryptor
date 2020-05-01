import string


ALPHABET = ""
__ALPHABET_DEFINED = False


def russian_lowercase_alphabet() -> str:
    return "".join(["%c" % (i + 1072 - (i > 6)) if i != 6 else "ё" for i in range(0, 32)])


def russian_uppercase_alphabet() -> str:
    return russian_lowercase_alphabet().upper()


def define_alphabet(language: str):
    global __ALPHABET_DEFINED
    if __ALPHABET_DEFINED:
        return
    __ALPHABET_DEFINED = True
    global ALPHABET
    if language == "en":
        ALPHABET = string.ascii_lowercase + string.digits + string.punctuation
    elif language == "ru":
        ALPHABET = russian_lowercase_alphabet() + string.digits + string.punctuation
    else:
        raise TypeError("Incorrect language")


def alphabet_positions() -> dict:
    return {ALPHABET[i]: i for i in range(len(ALPHABET))}
