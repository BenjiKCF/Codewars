def powers_of_two(n):
    b = []
    ans, i = 0, 0
    while ans < 2 ** n:
        ans = 2 **i
        i += 1
        b.append(ans)
    return b

print powers_of_two(4)#, [1, 2, 4, 8, 16])

def powers_of_two(n):
    return [2**x for x in range(n+1)]
