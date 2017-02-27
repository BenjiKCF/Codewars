# 9119 through the function, 811181

def square_digits(num):
    n = str(num)
    li = [int(n[i])*int(n[i]) for i in range(len(n))]
    return int(''.join(str(x) for x in li))

print square_digits(9119)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))
