def is_isogram(string):
    s = string.lower().replace('-','').replace(' ','')
    return len(set(s)) == len(s)
