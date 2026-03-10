"""Check if a sentence or string is a pangram
"""

def is_pangram(sentence):
    alphabet_sub_string_1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    alphabet_sub_string_2 = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
    alphabet_sub_string_3 = ['o', 'p', 'q', 'r', 's', 't', 'u']
    alphabet_sub_string_4 = ['v', 'w', 'y', 'x', 'z']

    alphabet_sub_string = alphabet_sub_string_1 + alphabet_sub_string_2 + alphabet_sub_string_3
    alphabet_sub_string += alphabet_sub_string_4
    #could import string then call a built in alphabet string 
    #alphabet = string.ascii_lowercase 
    
    lower_sentence = sentence.lower()

    if all(sub in lower_sentence for sub in alphabet_sub_string):
        return True
    return False