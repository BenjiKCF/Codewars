def shortcut( s ):
    return s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')

print shortcut('hello')#,'hll')

def shortcut(s):
    return s.translate(None, 'aeiou')
