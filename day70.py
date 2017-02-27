def dig_pow(n, p):
    nlist = [int(i) for i in str(n)]

    b = 0
    for i in nlist:
        a = i ** p
        b = b + a
        p+=1

    k = 1
    ans = 0
    while ans < b:
        ans = n * k
        k += 1
        if ans == b:
            return k - 1
    else:
        return -1

# (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

# b = n * k

print dig_pow(89, 1)#, 1)
print dig_pow(92, 1)#, -1)
print dig_pow(46288, 3)#, 51)

def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
