def iq_test(numbers):
    elist = []
    olist = []
    for i in numbers:
        if i % 2 == 0:
            elist.append(i)
        elif i % 2 != 0:
            olist.append(i)
    if len(elist) < len(olist):
        print numbers.index(elist[0])+1
    else:
        print numbers.index(olist[0])+1

numbers = (1, 2, 2)
iq_test(numbers)
