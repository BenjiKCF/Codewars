def is_square(n):
    return (abs(n) ** 0.5 % 1 ==0) and n > 0 

print is_square(-1) # => false
print is_square(3) # => false
print is_square(4)  # => true
print is_square(25) # => true
print is_square(26) # => false
