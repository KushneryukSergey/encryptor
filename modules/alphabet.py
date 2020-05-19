import string


class _ClassProperty(property):
    def __get__(self, obj, obj_type=None):
        return super(_ClassProperty, self).__get__(obj_type)
    def __set__(self, obj, value):
        super(_ClassProperty, self).__set__(type(obj), value)
    def __delete__(self, obj):
        super(_ClassProperty, self).__delete__(type(obj))


class Alphabet:
    ENGLISH = "en"
    RUSSIAN = "ru"
    _alphabet = ""
    _is_alphabet_defined = False
    _positions = {}

    @classmethod
    def _russian_lowercase_alphabet(cls) -> str:
        return "".join([chr(i + ord("а") - (i > 6) if i != 6 else ord("ё")) for i in range(33)])

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
    def get_languages(cls):
        return [cls.ENGLISH, cls.RUSSIAN]

    @classmethod
    def make_alphabet(cls, language: str) -> None:
        if cls._is_alphabet_defined:
            return
        if language == cls.ENGLISH:
            cls._alphabet = cls._english_alphabet()
        elif language == cls.RUSSIAN:
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
    def contains(cls, letter) -> bool:
        return letter in cls._alphabet

    @_ClassProperty
    def current_alphabet(cls) -> str:
        return cls._alphabet

    @classmethod
    def get_pos_by(cls, letter):
        return cls._positions.get(letter)

    @classmethod
    def shift_letter_by(cls, letter, shift):
        return cls.get_letter_by(cls.get_pos_by(letter) + shift)

    @classmethod
    def get_letter_by(cls, pos) -> str:
        return cls._alphabet[pos % len(cls._alphabet)]

