def last(*args):
    try:
        return args[-1][-1]
    except TypeError:
        return args[-1]



print last([1,2,3,4,5])#, 5)
print last("abcde")#, "e")
print last(1, "b", 3, "d", 5)#, 5)
print last(1)#, 5)

#    if len(args) == 1:
#        return args[-1][-1]
#    else:
#        return args[-1]

def last(*args):
    return args[-1] if not hasattr(args[-1], "__getitem__") else args[-1][-1]
