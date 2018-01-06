def numbers_with_digit_inside(x, d):
    n = [i for i in range(1, x+1) if str(d) in str(i)]
    return [len(n), sum(n), reduce(lambda x,y: x*y, n) if len(n)!=0 else 0]

print numbers_with_digit_inside(1, 0)

#x = 11
#d = 1
#Numbers: 1, 10, 11
#Return: [3, 22, 110]
