import math

def productFib1(prod):
    def F(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return F(n-1)+F(n-2)
    for i in range(prod):
            if F(i) * F(i+1) == prod:
                return [F(i), F(i+1), True]
            elif F(i) * F(i+1) >= prod:
                return [F(i), F(i+1), False]

print productFib(4895)
print productFib(5895)


def productFib(prod):
    f1 = 0
    f2 = 1
    while f1 * f2 < prod:
        f1, f2 = f2, f1 + f2
    return [f1, f2, prod == f1 * f2]
