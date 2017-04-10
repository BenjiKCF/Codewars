def square_or_square_root(arr):
    return [i**2 if i**0.5 %1 != 0 else int(i ** 0.5) for i in arr]




#[2,9,3,49,4,1]
print square_or_square_root([4,3,9,7,2,1])#, exp)
