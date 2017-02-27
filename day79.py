def nb_year(p0, percent, aug, p):
    p1 = p0
    i = 0
    while p1 < p:
        p1 = p1 + p1 * (percent/100.0) + aug
        i += 1
    return i



print nb_year(1500, 5, 100, 5000)#, 15)
print nb_year(1500000, 2.5, 10000, 2000000)#, 10)
print nb_year(1500000, 0.25, 1000, 2000000)#, 94)
