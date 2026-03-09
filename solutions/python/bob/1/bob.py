def response(hey_bob):
    if hey_bob.isupper():
        if hey_bob[-1] == '?':
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if "?" in hey_bob:
        if hey_bob[-1] == '.':
            return "Whatever."
        return 'Sure.'
    if not hey_bob.strip():
        return "Fine. Be that way!"
    return "Whatever."
            
