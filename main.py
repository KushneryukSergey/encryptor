from modules import cracking, frequencies, check_properties, cyphers
from modules.tools import input_text, output_text


ENCODE = "encode"
DECODE = "decode"
COUNT_F = "count_frequencies"
CRACK = "cracking"


def main():
    program_arguments = check_properties.argument_parsing()

    if program_arguments.working_mode == ENCODE:     # ENCODE WORKING MODE
        original_text = input_text(program_arguments.input_file)
        output_text(program_arguments.output_file,
                    cyphers.encode(program_arguments.cypher,
                                   original_text,
                                   program_arguments.key,
                                   program_arguments.language))

    elif program_arguments.working_mode == DECODE:   # DECODE WORKING MODE
        encrypted_text = input_text(program_arguments.input_file)
        output_text(program_arguments.output_file,
                    cyphers.decode(program_arguments.cypher,
                                   encrypted_text,
                                   program_arguments.key,
                                   program_arguments.language))

    elif program_arguments.working_mode == COUNT_F:  # COUNTING LETTER FREQUENCIES WORKING MODE
        encrypted_text = input_text(program_arguments.input_file)
        frequencies.count_frequencies(encrypted_text,
                                      program_arguments.language,
                                      program_arguments.freq_file)

    elif program_arguments.working_mode == CRACK:    # CRACKING CYPHER WORKING MODE
        encrypted_text = input_text(program_arguments.input_file)
        output_text(program_arguments.output_file,
                    cracking.crack(program_arguments.cypher,
                                   encrypted_text,
                                   program_arguments.language,
                                   program_arguments.freq_file))

    else:
        raise TypeError("Incorrect working mode")


if __name__ == "__main__":
    main()
