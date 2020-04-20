Project for first review for Python course in Moscow Institute of Physics and Technology

## Encryptor

### Abstract
Python project, that can encrypt and decrypt text, using Caesar, Vigenere and Vernam cyphers. Caesar and Vigenere cyphers can be cracked so (with some reservations)

### Usage
Use `python3 main.py -h` of `python3 main.py --help` to check usage of this project

### Working modes
    encode              In this mode you can encode your text
    decode              In this mode you can decode encrypted text, if you know key
    cracking            In this mode you can try to crack some text, if you know cypher
    count_frequencies   Necessary action to crack code, encoded by caesar cypher

You can precisely inspect working modes and other arguments by using `python3 main.py <WORKING MODE> --help`