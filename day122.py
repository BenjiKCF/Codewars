def row_sum_odd_numbers(n):
    total = sum([i for i in range(n+1)])
    return sum([1 + 2 * i for i in range(total)][-n:])



print row_sum_odd_numbers(2)#, 8)
print row_sum_odd_numbers(3)
print row_sum_odd_numbers(4)

#             1
#          3     5
#       7     9    11
#   13    15    17    19
#21    23    25    27    29

def row_sum_odd_numbers(n):
    #your code here
    return n ** 3
