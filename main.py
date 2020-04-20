import check_properties
import cyphers
import freq
import cracking
from tools import input_text, output_text


PROGRAM_ARGUMENTS = check_properties.argument_parsing()

if PROGRAM_ARGUMENTS.WORKING_MODE == "encode":                # ENCODE WORKING MODE
    original_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(cyphers.encode(PROGRAM_ARGUMENTS.CYPHER,
                               original_text,
                               PROGRAM_ARGUMENTS.KEY,
                               PROGRAM_ARGUMENTS.LANGUAGE),
                PROGRAM_ARGUMENTS.OUTPUT_FILE)

elif PROGRAM_ARGUMENTS.WORKING_MODE == "decode":              # DECODE WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(cyphers.decode(PROGRAM_ARGUMENTS.CYPHER,
                               encrypted_text,
                               PROGRAM_ARGUMENTS.KEY,
                               PROGRAM_ARGUMENTS.LANGUAGE),
                PROGRAM_ARGUMENTS.OUTPUT_FILE)

elif PROGRAM_ARGUMENTS.WORKING_MODE == "count_frequencies":   # COUNTING LETTER FREQUENCIES WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    freq.count_frequencies(encypted_text, PROGRAM_ARGUMENTS.LANGUAGE)

elif PROGRAM_ARGUMENTS.WORKING_MODE == "cracking":            # CRACKING CYPHER WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(cracking.crack(PROGRAM_ARGUMENTS.CYPHER, encrypted_text))

else:
    raise TypeError("Incorrect working mode")
