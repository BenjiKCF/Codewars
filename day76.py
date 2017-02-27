def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    else:
        i = (end_number - begin_number) / step
        ans = 0
        for j in range(i+1):
            ans = ans + begin_number
            begin_number += step
        return ans

print sequence_sum(2, 6, 2)#, 12)
print sequence_sum(1, 5, 1)#, 15)
