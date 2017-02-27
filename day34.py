def is_opposite(s1,s2):
    s1a = []
    for char in s1:
        if char.isupper():
            s1a.append(char.lower())
        elif char.islower():
            s1a.append(char.upper())
        else:
            s1a.append(char)
    s1a = ''.join(s1a)
    if s1a == s2 and s1 != '':
        return True
    else:
        return False

print is_opposite("","")

def is_opposite(s1, s2):
    return False if not(s1 or s2) else s1.swapcase() == s2
