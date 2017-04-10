def s(x,n):
    if n==1:
        return 1 if 1<=x<=6 else 0
    else:
        return sum([s(x-i, n-1) for i in range(1,7)])

def rolldice_sum_prob(x, n):
    return 1.0*s(x,n)/6**n

print rolldice_sum_prob(11, 2)#, 0.055555555555)
