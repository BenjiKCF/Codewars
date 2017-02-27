def min(arr):
    smallest = arr[0]
    for i in arr:
        if i < smallest:
            smallest = i
    return smallest

def max(arr):
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    return largest


print max([4,6,2,1,9,63,-134,566])# returns 566
print min([-52, 56, 30, 29, -54, 0, -110])# returns -110
print max([5])# returns 5
print min([42, 54, 65, 87, 0])# returns 0
print min([1, 2, 3, 4, 5, 10])#, 1)

def m(arr):
    return min(arr)

def m(arr):
    return max(arr)

pass
# fuck, this is so clever^^
