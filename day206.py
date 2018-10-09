def is_prime(num):
    t = 0
    if num <= 1:
        return False

    for i in range(2, num):
        print i
        if num % i == 0:
            t += 1

    if t != 0:
        return False
    else:
        return True


print is_prime(2)
