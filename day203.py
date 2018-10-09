def divisors(integer):
    d = []
    for i in range(2, integer):
        if integer % i == 0:
            d.append(int(i))
    if len(d)==0:
        return str(integer) + " is prime"
    else:
        return str(d)

#print divisors(12)#, [2, 3, 4, 6])
print divisors(250); #should return [5]
