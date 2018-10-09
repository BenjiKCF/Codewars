def has_unique_chars(string):
    myset = set(string.lower())
    if len(myset) == len(string):
        return True
    else:
        return False

#print has_unique_chars("abcdef")#,True)
print has_unique_chars("abcdefA")#,True)
print has_unique_chars(",")
print has_unique_chars(" ")

def has_unique_chars(s):
    return len(s) == len(set(s))
