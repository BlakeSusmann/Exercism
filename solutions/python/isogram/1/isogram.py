"""Functions need to determine if a word or sentence 
is a isogram (excluding repeats of hypens and spaces)

Isogram is a word or sentence that has no repeating 
letters
"""

def is_isogram(string):
    """Calculate and process string input for isogram check 

    param string: str - input word or words. 
    return: boolean - if input is isogram
    """

    #this lowers string characters and filters out spaces and hypens 
    cleaned_string = [char.lower() for char in string if char.isalpha()]
    #this creates a set string container that will not allow 
    #for duplicates, then checks the length of that set.container 
    #compared to the length of the container(w/unset_string) 
    #if lengths don't match input string is not an isogram
    #due to repeating alpabet characters
    return len(set(cleaned_string)) == len(cleaned_string)
    
        