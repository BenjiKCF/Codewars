def remove_smallest(numbers):
    l = [(index, value) for index, value in enumerate(numbers)]
    n = sorted(numbers)
    for i in range(len(numbers)):
        if n[0] == l[i][1]:
            numbers.pop(i)
            break
    return numbers

def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers
