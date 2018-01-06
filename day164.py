def sum_pairs(ints, s):
    for i in ints:
        for j in ints:
            if i + j == s:
                return [i, j]
    else:
        return None

print sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
#== [3, 7]
print sum_pairs([4, 3, 2, 3, 4],         6)
print sum_pairs([20, -13, 40], -7)# == None
