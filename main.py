from modules import cracking, frequencies, check_properties, cyphers
from modules.tools import read_text, print_text
from modules.alphabet import Alphabet


def main():
    program_arguments = check_properties.argument_parsing()
    Alphabet.make_alphabet(program_arguments.language)

    if program_arguments.working_mode == 'encode':
        original_text = read_text(program_arguments.input_file)
        encrypted_text = cyphers.encode(program_arguments.cypher,
                                        original_text,
                                        program_arguments.key,
                                        program_arguments.language)
        print_text(program_arguments.output_file, encrypted_text)

    elif program_arguments.working_mode == 'decode':
        encrypted_text = read_text(program_arguments.input_file)
        original_text = cyphers.decode(program_arguments.cypher,
                                       encrypted_text,
                                       program_arguments.key,
                                       program_arguments.language)
        print_text(program_arguments.output_file, original_text)

    elif program_arguments.working_mode == 'count_frequencies':
        encrypted_text = read_text(program_arguments.input_file)
        frequencies.save_frequencies(encrypted_text,
                                     program_arguments.language,
                                     program_arguments.freq_file)

    elif program_arguments.working_mode == 'cracking':
        encrypted_text = read_text(program_arguments.input_file)
        cracked_text = cracking.break_cypher(program_arguments.cypher,
                                             encrypted_text,
                                             program_arguments.language,
                                             program_arguments.freq_file)
        print_text(program_arguments.output_file, cracked_text)

    else:
        raise TypeError('Incorrect working mode')


if __name__ == '__main__':
    main()
