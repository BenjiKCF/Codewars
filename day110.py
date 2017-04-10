import itertools

def longest(s1, s2):
    return  ''.join(ch for ch, _ in itertools.groupby(sorted(s1+s2)))


print longest("aretheyhere", "yestheyarehere")#, "aehrsty")


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))

print longest("aretheyhere", "yestheyarehere")
