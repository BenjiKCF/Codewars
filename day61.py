def digitize(n):
    return map(int, str(n)[::-1])

print digitize(35231) #,[1,3,2,5,3])
