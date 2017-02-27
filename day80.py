def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number and step < 0:
        return sum(xrange(begin_number, end_number - 1, step))
    else:
        return sum(xrange(begin_number, end_number + 1, step))


print sequence_sum(2, 6, 2) == 12
print sequence_sum(1, 5, 1) == 15
print sequence_sum(-1, -5, -3) == -5
print sequence_sum(-24, -2, 22) == -26
print sequence_sum(2, 2, 2) == 2
print sequence_sum(2, 6, 2) == 12 #(= 2 + 4 + 6)
print sequence_sum(1, 5, 1) == ( 1 + 2 + 3 + 4 + 5)
print sequence_sum(1, 5, 3) == 5 #(= 1 + 4)

def sequence_sum(s,e,t):n=(e-s)/t;return n>=0and-~n*(2*s+n*t)/2
