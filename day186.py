def ones_complement(binary_number):
    return  ''.join([str(0) if i == str(1) else str(1) for i in binary_number])

print ones_complement("1101")
