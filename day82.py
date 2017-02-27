def inverse_slice(items, a, b):
    return [i for i in items if i not in items[a:b]]



print inverse_slice([12, 14, 63, 72, 55, 24], 2, 4)#, [12, 14, 55, 24])
