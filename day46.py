
s = '45385593107843568'

def fake_bin(x):
    a = []
    for i in x:
        print i
        if int(i) < 5:
            a.append('0')
        elif int(i) >= 5:
            a.append('1')
    return ''.join(a)

print fake_bin(s)

def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)
