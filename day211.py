def to_weird_case(string):
    string = [i for i in string.split(' ')]

    new=[]

    for word in string:
        for i in range(len(word)):
            if i % 2 ==0:
                new.append(word[i].upper())
            else:
                new.append(word[i])
        new.append(' ')

    return ''.join(new[:-1])

print to_weird_case('This is a test')#, 'ThIs')

def to_weird_case_word(string):
    return "".join(c.upper() if i%2 == 0 else c for i, c in enumerate(string.lower()))

def to_weird_case(string):
    return " ".join(to_weird_case_word(str) for str in string.split())
