def persistence(num, count=1):
    if len(str(num)) == 1:
        return 0
    numlist = [ch for ch in str(num)]
    newnum = reduce(lambda x,y: int(x)*int(y), numlist)
    if len(str(newnum)) != 1:
        return persistence(newnum, count+1)
    else:
        return count

print persistence(39)

import operator
def persistence(n):
    i = 0
    while n>=10:
        n=reduce(operator.mul,[int(x) for x in str(n)],1)
        i+=1
    return i
