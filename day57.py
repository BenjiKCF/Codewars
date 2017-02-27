def sum_array(arr):
    if not arr:
        return 0
    else:
        return sum(sorted(arr)[1:len(arr)-1])

print sum_array(None)
print sum_array([6, 2, 1, 8, 10]) # 16
