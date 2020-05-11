import string

ENGLISH = "en"
RUSSIAN = "ru"


class Alphabet:
    _alphabet = ""
    _is_alphabet_defined = False
    _positions = {}

    @classmethod
    def _russian_lowercase_alphabet(cls) -> str:
        return "".join([chr(i + ord("а") - (i > 6) if i != 6 else ord("ё")) for i in range(0, 32)])

    @classmethod
    def _russian_uppercase_alphabet(cls) -> str:
        return cls._russian_lowercase_alphabet().upper()

    @classmethod
    def _mixed_russian_alphabet(cls) -> str:
        return "".join([upper_letter + lower_letter for upper_letter, lower_letter in
                        zip(cls._russian_uppercase_alphabet(), cls._russian_lowercase_alphabet())])

    @classmethod
    def _russian_alphabet(cls) -> str:
        return cls._russian_uppercase_alphabet() + cls._russian_lowercase_alphabet()

    @classmethod
    def _english_lowercase_alphabet(cls) -> str:
        return string.ascii_lowercase

    @classmethod
    def _english_uppercase_alphabet(cls) -> str:
        return string.ascii_uppercase

    @classmethod
    def _mixed_english_alphabet(cls) -> str:
        return "".join([upper_letter + lower_letter for upper_letter, lower_letter in
                        zip(cls._english_uppercase_alphabet(), cls._english_lowercase_alphabet())])

    @classmethod
    def _english_alphabet(cls) -> str:
        return cls._english_uppercase_alphabet() + cls._english_lowercase_alphabet()

    @classmethod
    def size(cls):
        return len(cls._alphabet)

    @classmethod
    def make_alphabet(cls, language: str) -> None:
        if cls._is_alphabet_defined:
            return
        if language == ENGLISH:
            cls._alphabet = cls._english_alphabet()
        elif language == RUSSIAN:
            cls._alphabet = cls._russian_alphabet()
        else:
            raise TypeError("Incorrect language")
        cls._alphabet += string.digits + string.punctuation
        cls._make_alphabet_positions()
        cls._is_alphabet_defined = True

    @classmethod
    def _make_alphabet_positions(cls) -> None:
        cls._positions = {letter: index for index, letter in enumerate(cls._alphabet)}

    @classmethod
    def get_pos_by(cls, letter):
        return cls._positions.get(letter, None)

    @classmethod
    def get_letter_by(cls, pos) -> str:
        return cls._alphabet[pos % len(cls._alphabet)]


if __name__ == "__main__":
    print("{0:c}".format(1072))
