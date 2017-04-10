def is_digit(n):
    ch = [i for i in n]
    if n == "" or len(ch) > 1:
        return False
    for j in ch:
        if not j.isdigit():
            return False
    else:
        return True


print is_digit("")#, False)
print is_digit("7")
print is_digit("a5")#, False)
print is_digit("5a")
print is_digit("14")

def is_digit(n):
    return n.isdigit() and len(n)==1
