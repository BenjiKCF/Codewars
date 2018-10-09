def digital_root(n):
    n = n
    while counter(n) != True:
        n = summer(n)
    return n

def counter(n):
    if len(str(n)) != 1:
        return False
    else:
        return True

def summer(n):
    num_sum = 0
    for i in str(n):
        num_sum += int(i)
    return num_sum




print digital_root(16)#, 7 )
print digital_root(132189)

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
