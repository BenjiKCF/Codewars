s = '!!'

def product(s):
    return len([i for i in s if i == '!']) * len([i for i in s if i == '?'])

print product(s)

def product(s):
    return s.count("?")*s.count("!")
