import argparse
from modules.alphabet import ENGLISH, RUSSIAN


def argument_parsing():
    cf_parser = argparse.ArgumentParser(add_help=False)
    cf_parser.add_argument("-i", "--input_file", default=None,
                           help="<INPUT_FILE> with text to decode, encode or count letter frequencies")
    cf_parser.add_argument("-l", "--language", default=ENGLISH, choices=[ENGLISH, RUSSIAN],
                           help="text language, default English")
    base_parser = argparse.ArgumentParser(parents=[cf_parser], add_help=False)
    base_parser.add_argument("-o", "--output_file", default=None,
                             help="<OUTPUT_FILE> to put encoded or decode text")
    base_parser.add_argument("-c", "--cypher", choices=["caesar", "vigenere", "vernam"], default="caesar",
                             help="<CYPHER> type. In encode and decode modes default is caesar with key = 3")

    main_parser = argparse.ArgumentParser()
    main_subparsers = main_parser.add_subparsers(dest="working_mode", help="Choose <WORKING_MODE> of program")
    parser_encode = main_subparsers.add_parser("encode", parents=[base_parser],
                                               help="In this mode you can encode your text")
    parser_encode.add_argument("-k", "--key", default="3",
                               help="<KEY> to encode text. Required number for caesar, word for vigenere\
                                      and text with length >= length of text to be encrypted/decrypted")

    parser_decode = main_subparsers.add_parser("decode", parents=[base_parser],
                                               help="In this mode you can decode encrypted text, if you know key")
    parser_decode.add_argument("-k", "--key", default="3",
                               help="<KEY> to decode text. Required number for caesar, word for vigenere \
                                    and text with length >= length of text to be encrypted/decrypted")

    parser_cracking = main_subparsers.add_parser("cracking", parents=[base_parser],
                                                 help="In this mode you can try to crack some text, if you know cypher")
    parser_cracking.add_argument("-f", "--frequencies", dest="freq_file", default="./resources/frequencies_data.json",
                                 help="<FREQ_FILE> - json file with frequencies to crack caesar cypher. \
                                      In file should lie dict w\\ elements like ('letter': frequency). \
                                      Default file is frequencies_data.json")

    parser_cf = main_subparsers.add_parser("count_frequencies", parents=[cf_parser],
                                           help="Necessary action to crack code, encoded by caesar cypher")
    parser_cf.add_argument("-f", "--frequencies", dest="freq_file", default="./resources/frequencies_data.json",
                                 help="<FREQ_FILE> - json file where frequencies will be written. \
                                      Default file is frequencies_data.json")
    ###########################################################################
    # PARSING ARGUMENTS
    args = main_parser.parse_args()
    return args
