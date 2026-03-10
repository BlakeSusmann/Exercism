"""Check if a sentence or string is a pangram
"""

def is_pangram(sentence):
    Alphabet_sub_string_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    Alphabet_sub_string_2 = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
    Alphabet_sub_string_3 = ['o', 'p', 'q', 'r', 's', 't', 'u']
    Alphabet_sub_string_4 = ['v', 'w', 'y', 'x', 'z']

    Alphabet_sub_string = Alphabet_sub_string_1 + Alphabet_sub_string_2 + Alphabet_sub_string_3
    Alphabet_sub_string += Alphabet_sub_string_4
    #could import string then call a built in alphabet string 
    #alphabet = string.ascii_lowercase 
    
    lower_sentence = sentence.lower()

    if all(sub in lower_sentence for sub in Alphabet_sub_string):
        return True
    return False