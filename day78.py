def iq_test(numbers):
    num = map(int, numbers.split(' '))
    elist, olist = [], []
    for i in num:
        if i % 2 == 0:
            elist.append(i)
        else:
            olist.append(i)
    if len(elist) > len(olist):
        return num.index(olist[0]) + 1
    else:
        return num.index(elist[0]) + 1

print iq_test("2 4 7 8 10")#,3)

def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
