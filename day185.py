def sum_of_n(n):
    ans = []
    accum = 0
    if n >= 0:
        for i in range(n+1):
            accum += i
            ans.append(accum)
        return ans
    else:
        for i in range(abs(n)+1):
            accum += i
            ans.append(-accum)
        return ans
print sum_of_n(3)
print sum_of_n(-4)

def sum_of_n(n):
    return [(-1 if n < 0 else 1) * sum(xrange(i+1)) for i in xrange(abs(n)+1)]
