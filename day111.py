def xo(s):
    return True if s.count('o') + s.count('O') == s.count('x') + s.count('X') else False

print xo("ooxx")# => true
print xo("xoooxx")# => false

def xo(s):
    return s.lower().count('o') == s.lower().count('x')
