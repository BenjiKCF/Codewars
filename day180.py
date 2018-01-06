def count(n):
    temp = 1
    xlist = range(1, n+1)
    for i in xlist:
        temp = i * temp
    return len(str(temp))

print count(5000)
