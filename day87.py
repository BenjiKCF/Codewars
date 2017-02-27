def disemvowel(string):
    return ''.join([ '' if ch in 'AEIOUaeiou' else ch for ch in string])



print disemvowel("This website is for losers LOL!")
                             # "Ths wbst s fr lsrs LL!")

def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")
