def find_outlier(integers):
    odd = []
    even = []
    for i in integers:
        if i % 2 ==0:
            odd.append(i)
        else:
            even.append(i)
    if len(odd) < len(even):
        return odd[0]
    else:
        return even[0]

print find_outlier([2,6,8,10,3])#, 3)
