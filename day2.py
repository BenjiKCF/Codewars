def positive_sum(arr):
    mylist = []
    i = 0
    for i in arr:
        if i >= 1:
            mylist.append(i)
    return sum(mylist)

positive_sum([1,-4,7,12])
