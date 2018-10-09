def choose_best_sum(t, k, ls):
    from itertools import combinations

    comb = list(combinations(ls, k))

    sum_comb = []
    new_sum_comb = []

    for j in range(len(comb)):
        sum_comb.append(sum([int(i) for i in comb[j]]))

    for k in sum_comb:
        if k <= t:
            new_sum_comb.append(k)
    return max(new_sum_comb) if new_sum_comb != [] else None



xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# print choose_best_sum(230, 4, xs)#, 230)

def combinations(n, list, combos=[]):
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos

print combinations(3, xs)
