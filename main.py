from modules import cracking, frequencies, check_properties, cyphers
from modules.tools import input_text, output_text


PROGRAM_ARGUMENTS = check_properties.argument_parsing()

if PROGRAM_ARGUMENTS.WORKING_MODE == "encode":                # ENCODE WORKING MODE
    original_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(PROGRAM_ARGUMENTS.OUTPUT_FILE,
                cyphers.encode(PROGRAM_ARGUMENTS.CYPHER,
                               original_text,
                               PROGRAM_ARGUMENTS.KEY,
                               PROGRAM_ARGUMENTS.LANGUAGE))

elif PROGRAM_ARGUMENTS.WORKING_MODE == "decode":              # DECODE WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(PROGRAM_ARGUMENTS.OUTPUT_FILE,
                cyphers.decode(PROGRAM_ARGUMENTS.CYPHER,
                               encrypted_text,
                               PROGRAM_ARGUMENTS.KEY,
                               PROGRAM_ARGUMENTS.LANGUAGE))

elif PROGRAM_ARGUMENTS.WORKING_MODE == "count_frequencies":   # COUNTING LETTER FREQUENCIES WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    frequencies.count_frequencies(encrypted_text,
                                  PROGRAM_ARGUMENTS.LANGUAGE,
                                  PROGRAM_ARGUMENTS.FREQ_FILE)

elif PROGRAM_ARGUMENTS.WORKING_MODE == "cracking":            # CRACKING CYPHER WORKING MODE
    encrypted_text = input_text(PROGRAM_ARGUMENTS.INPUT_FILE)
    output_text(PROGRAM_ARGUMENTS.OUTPUT_FILE,
                cracking.crack(PROGRAM_ARGUMENTS.CYPHER,
                               encrypted_text,
                               PROGRAM_ARGUMENTS.LANGUAGE,
                               PROGRAM_ARGUMENTS.FREQ_FILE))

else:
    raise TypeError("Incorrect working mode")
