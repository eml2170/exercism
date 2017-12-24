import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase
    counter = set()
    for c in sentence.lower():
        if c in alphabet:
            counter.add(c)
    return len(counter) == 26
