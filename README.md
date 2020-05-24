Project for first review for Python course in Moscow Institute of Physics and Technology

## Encryptor

### Abstract
Python project, that can encrypt and decrypt text, using Caesar, Vigenere and Vernam cyphers. Caesar and Vigenere cyphers can be cracked so (with some reservations)

### Usage
Use `python3 main.py -h` or `python3 main.py --help` to check usage of this project

### Working modes
    encode              In this mode you can encode your text
    decode              In this mode you can decode encrypted text, if you know key
    cracking            In this mode you can try to crack some text, if you know cypher
    count_frequencies   Necessary action to crack code, encoded by caesar cypher

### Input and output
With writing `-i` or `--input_file` you can define file to read text from. 
Likewise, `-o` or `--output_file` options define output file for text. By default console input and output are used
P.S. You can mix them (e.g. use file input and console output)

### Counting frequencies and cracking cyphers
`python3 main.py count_frequencies` will help you count letter frequencies from any text you want.
Add this text by `-i` or `--input_file`, or write it through console. Pay attention, that the bigger is text
the better `cracking` mode works. However, cracking may be less accurate with small texts, be careful

You can find some texts in `texts` folder and use them to count letter frequencies

`-f` or `--frequencies` option will help you if you want to save letter frequencies in external file. If you want 
to use external file for cracking, it should be json file with dict containing pairs of ('letter': frequency). Don't 
forget to choose language of text if you need it, by default it's english

Now available only cracking of Caesar cypher; Vigenere cypher will be added soon


### Extra
You can precisely inspect working modes and other arguments by using `python3 main.py <WORKING MODE> --help`

### Testing strings
You can check how code works with next command lines

>All commands should be executed from root folder

Caesar cypher test
```
python3 main.py encode -o resources/caesar_test.txt -c caesar -k 3
python3 main.py decode -i resources/caesar_test.txt -c caesar -k 3
```
Vigenere cypher test
```
python3 main.py encode -o resources/vigenere_test.txt -c vigenere -k hello
python3 main.py decode -i resources/vigenere_test.txt -c vigenere -k hello
```
Vernam cypher test
```
python3 main.py encode -o resources/vernam_test.txt -c vernam -k resources/vernam_key.txt
python3 main.py decode -i resources/vernam_test.txt -c vernam -k resources/vernam_key.txt
```

> You'll find encrypted text in relevant file in every case. After using first command you should input your text and
> push Ctrl+D. After using second command you'll get back your text