def to_alternating_case(string):
    new = []
    for ch in string:
        if ch.isalpha() and ch == ch.upper():
            new.append(ch.lower())
        else:
            new.append(ch.upper())
    return ''.join(new)

print to_alternating_case("hello world")#, "HELLO WORLD")
print to_alternating_case("HELLO WORLD")#, "hello world")

def to_alternating_case(string):
    return string.swapcase()
