def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i+1]) == sum(arr[i:]):
            return i
    else:
        return -1

print find_even_index([1,2,3,4,3,2,1])# ,3)
