def repeats(arr):
    xlist = []
    for i in arr:
        no = arr.count(i)
        if no == 1:
            xlist.append(i)
    return sum(xlist)

print repeats([4,5,7,5,4,8])
