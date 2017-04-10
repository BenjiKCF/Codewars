def find_missing_number(sequence):
    if sequence == '':
        return 0
    else:
        for ch in sequence:
            if ch.isalpha() or ch == '_':
                return 1
        sequence = map(int, sequence.split())
        a = []
        for i in range(1, max(sequence)+1):
            if i not in sequence:
                a.append(i)
        return a[0] if len(a) >= 1 else 0


print find_missing_number("1 2 3 5")#4, "It must work for missing middle terms")
# range(1, max(map(int, sequence.split())) +1)
print find_missing_number("1 5") # 2
print find_missing_number("1 2 3 4") #0
print find_missing_number("")#0
print find_missing_number("2 1 4 3 a") # 1
print find_missing_number("2.0 a") #1
print find_missing_number("2 6 4 5 3") #1
print find_missing_number("2 3 4 5")#,1,
print find_missing_number("16 9 4 20 18 12 8 1 7 14 3 13 10 2 17 5 19 6 15 21")
print find_missing_number("_______")

def find_missing_number(sequence):
    if not sequence:
        return 0
    try:
        sequence = set(int(a) for a in sequence.split())
    except ValueError:
        return 1
    for b in xrange(1, max(sequence) + 1):
        if b not in sequence:
            return b
    return 0
