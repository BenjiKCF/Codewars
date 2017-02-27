def count_positives_sum_negatives(arr):
    if arr != [] or sum(arr) != 0:
        return [len([i for i in arr if i > 0]), sum(i for i in arr if i < 0)]
    else:
        return []

print count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) #[10,-65]

def count_positives_sum_negatives(arr):
    return [len([x for x in arr if x > 0])] + [sum(y for y in arr if y < 0)] if arr else []
