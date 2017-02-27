def find_average(array):
    if len(array) != 0:
        return sum(array)/len(array)
    else:
        return 0

array = [ 1, 2, 3 ]
print find_average(array)

def find_average(array):
    return sum(array) / len(array) if array else 0
