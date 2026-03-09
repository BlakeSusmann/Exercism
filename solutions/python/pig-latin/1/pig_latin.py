def translate(text):
    
    def translate_word(word):
        if word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            return word + 'ay'
            
        if 'qu' in word:
            q_location = word.find('q') 
            word_start_num = q_location + 2
            if q_location == 2:
                return word[1:] + word[0] + 'ay'
            return word[word_start_num:] + word[:word_start_num] + 'ay'
        
        if word.startswith('th'):
            if word.startswith('thr'):
                return word[3:] + 'thray'
            return word[2:] + 'thay'
        
        if 'y' in word:
            y_location = word.find('y')
            if y_location == 0:
                return word[1:] + 'yay'
            return word[y_location:] + word[:y_location] + 'ay'
   
        vowels = ('a', 'e', 'i', 'o', 'u')
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + 'ay'
                
    return ' '.join(translate_word(w) for w in text.split())
    
    
        