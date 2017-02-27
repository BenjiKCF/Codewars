def replace_exclamation(s):
    vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    ns = ""
    for ch in s:
        if ch in vowel:
            ns = ns + '!'
        else:
            ns = ns + ch
    return ns



print replace_exclamation("Hi!")# , "H!!")

def replace_exclamation(s):
    return ''.join('!' if c in 'aeiouAEIOU' else c for c in s)
