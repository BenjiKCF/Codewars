def unique_in_order(iterable):
    if len(iterable) == 0:
        return []
    nw = []
    nw.append(iterable[0])
    lw = iterable[0]
    for i in iterable[1:]:
        if i == lw:
            pass
        else:
            lw = i
            nw.append(i)
    return nw

print unique_in_order('AAAABBBCCDAABBB')#, ['A','B','C','D','A','B'])
print unique_in_order('')
