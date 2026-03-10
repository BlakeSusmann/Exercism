"""Check if a sentence or string is a pangram
"""

def is_pangram(sentence):
    Alphabet_substring1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    Alphabet_substring2 = ['h', 'i', 'j', 'k', 'l', 'm', 'n']
    Alphabet_substring3 = ['o', 'p', 'q', 'r', 's', 't', 'u']
    Alphabet_substring4 = ['v', 'w', 'y', 'x', 'z']

    Alphabet_substring = Alphabet_substring1 + Alphabet_substring2 + Alphabet_substring3
    Alphabet_substring += Alphabet_substring4
    #could import string then call a built in alphabet string 
    #alphabet = string.ascii_lowercase 
    
    lower_sentence = sentence.lower()

    if all(sub in lower_sentence for sub in Alphabet_substring):
        return True
    return False