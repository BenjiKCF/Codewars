def high_and_low(numbers):
    return ' '.join((str(max([int(i) for i in numbers.split(' ')])), str(min([int(i) for i in numbers.split(' ')]))))


print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

def high_and_low(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))
