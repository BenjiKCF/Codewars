import string

def find_missing_letter(chars):
    big = string.ascii_lowercase
    if chars[0].islower():
        return find_lower(chars)
    else:
        return find_upper(chars)

def find_lower(chars):
    low = string.ascii_lowercase
    ninit = []

    for char in chars:
        init = low.index(char)
        ninit.append(init)

    return low[sum(xrange(ninit[0],ninit[-1]+1)) - sum(ninit)]

def find_upper(chars):
    low = string.ascii_uppercase
    ninit = []

    for char in chars:
        init = low.index(char)
        ninit.append(init)

    return low[sum(xrange(ninit[0],ninit[-1]+1)) - sum(ninit)]

print find_missing_letter(['a','b','c','d','f'])#, 'e')

def find_missing_letter(c):
    # for i in range(len(c)-1)
        # if ord(c[i])+1 != ord(c[i+1])
            # next(chr(ord(c[i])+1)
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
