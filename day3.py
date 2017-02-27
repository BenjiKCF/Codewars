def sum_two_smallest_numbers(numbers):
    n = sorted(numbers)
    return n[0] + n[1]

print sum_two_smallest_numbers([7, 15, 12, 18, 22])
