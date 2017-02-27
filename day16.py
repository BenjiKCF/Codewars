

def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum == target and i != j:
                return [i, j]



print two_sum([1,2,3], 4)
# [0,2]
