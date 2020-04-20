def russian_lowercase_alphabet() -> str:
    return "".join(["%c" % (i + 1072 - (i > 6)) if i != 6 else "ё" for i in range(0, 32)])


def russian_uppercase_alphabet() -> str:
    return russian_lowercase_alphabet().upper()


def define_alphabet(language: str) -> str:
    import string
    if str == "en":
        return string.ascii_lowercase + string.digits + string.punctuation
    elif str == "ru":
        return russian_lowercase_alphabet() + string.digits + string.punctuation
    else:
        raise TypeError("Incorrect language")



