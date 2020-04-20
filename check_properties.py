import argparse


def argument_parsing():
    cf_parser = argparse.ArgumentParser(add_help=False)
    cf_parser.add_argument("-i", "--input_file", dest="INPUT_FILE", type=str, default="input.txt",
                           help="<INPUT_FILE> with text to decode, encode or count letter frequencies")
    base_parser = argparse.ArgumentParser(parents=[cf_parser], add_help=False)
    base_parser.add_argument("-o", "--output_file", dest="OUTPUT_FILE", type=str, default="output.txt",
                             help="<OUTPUT_FILE> to put encoded or decode text")
    base_parser.add_argument("-c", "--cypher", dest="CYPHER", choices=["caesar", "vigenere", "vernam"],
                             default="caesar", help="<CYPHER> type. In encode and decode modes default is caesar with \
                                                    key = 3")
    base_parser.add_argument("-l", "--language", dest="LANGUAGE", type=str, default="en", choices=["en", "ru"],
                             help="text language, default English")
    main_parser = argparse.ArgumentParser()
    main_subparsers = main_parser.add_subparsers(dest="WORKING_MODE", help="Choose <WORKING_MODE> of program")
    parser_encode = main_subparsers.add_parser("encode", parents=[base_parser],
                                               help="In this mode you can encode your text")
    parser_encode.add_argument("-k", "--key", dest="KEY", default="3",
                               help="<KEY> to encode text. Required number for caesar, word for vigenere\
                                      and text with length >= length of text to be encrypted/decrypted")
    parser_decode = main_subparsers.add_parser("decode", parents=[base_parser],
                                               help="In this mode you can decode encrypted text, if you know key")
    parser_decode.add_argument("-k", "--key", dest="KEY", default="3",
                               help="<KEY> to decode text. Required number for caesar, word for vigenere \
                                    and text with length >= length of text to be encrypted/decrypted")
    parser_cracking = main_subparsers.add_parser("cracking", parents=[base_parser],
                                                 help="In this mode you can try to crack some text, if you know cypher")
    parser_cf = main_subparsers.add_parser("count_frequencies", parents=[cf_parser],
                                           help="Necessary action to crack code, encoded by caesar cypher")

    ###########################################################################
    # PARSING ARGUMENTS
    args = main_parser.parse_args()
    if (args.WORKING_MODE == "encode" or args.WORKING_MODE == "encode") and args.CYPHER == "caesar":
        args.KEY = int(args.KEY)
    return args
