def convert(st):
    word = []
    for ch in st:
        if ch == 'a':
            word.append('o')
        elif ch == 'o':
            word.append('u')
        else:
            word.append(ch)
    return ''.join(word)

print convert('codewars')#, 'cudewors')
# a like o and o like a u

def convert(st):
    return st.replace('o','u').replace('a','o')
