def square_sum(numbers):
    if numbers:
        return reduce(lambda x,y: x+y, map(lambda x: x**2, numbers))
    else:
        return 0

print square_sum([0, 3, 4, 5])#, 50)

def square_sum(numbers):
    return sum(x**2 for x in numbers)
