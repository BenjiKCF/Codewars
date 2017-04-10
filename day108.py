def find_next_square(sq):
    return int((sq ** 0.5 + 1) ** 2) if (sq ** 0.5 + 1) ** 2 % 1 == 0 else -1

print find_next_square(121)#, 144,
