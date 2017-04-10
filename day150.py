def animals(heads, legs):
    cow = (legs - 2 * heads) / 2
    chick = heads - cow
    if cow % 1 == 0 and chick % 1 == 0 and cow >= 0 and chick >= 0:
        return chick, cow
    else:
        return 'No solutions'

print animals(72, 200)#, (44, 28))
