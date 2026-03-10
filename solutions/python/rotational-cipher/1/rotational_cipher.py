"""Function called 'rotate' to perform a Ceasar Cipher
with text, key input 
text string to key 
key rotation of cipher

Ceasar Cipher produces a keyed response from a cipher rotation 
of the alphabet
"""

# get alaphabet .string ascii list
# string .maketrans for mapping keyed abc to reg abc
import string

def rotate(text, key):
    # get lower case letters string
    alphabet = string.ascii_lowercase
    # create keyed or shifted alphabet key starts with shift to tail 
    # then adds '+' front of alphabet to shift point finishs shifted/keyed alphabet
    keyed_alphabet = alphabet[key % 26:] + alphabet[:key % 26]

    # create mapping for lower case and upper case
    # alphabet (from string.<call>
    # to and from reg alphabet order to shifted/keyed alphabet/alphabet order  
    mapping_table = str.maketrans(alphabet + alphabet.upper(), keyed_alphabet + keyed_alphabet.upper())

    return text.translate(mapping_table)

    