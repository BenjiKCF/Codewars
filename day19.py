s = "abcd\nefgh\nijkl\nmnop"
print s + '\n'

def diag_1_sym(s):
    splited = s.split('\n')
    matelem = len(splited)      #4
    elemlen = len(splited[0])   #4
    diag = [''.join ([splited[i][j] for i in range(matelem)]) + '\n' for j in range(matelem)]
    last = diag[-1][:-1]
    diag.pop()
    diag.append(last)
    return''.join(diag)

print diag_1_sym(s)
print '\n' + '\n'

def rot_90_clock(s):
    splited = s.split('\n')
    matelem = len(splited)      #4
    elemlen = len(splited[0])   #4
    ndiag = ''.join([''.join ([splited[i][j] for i in range(matelem)]) + '\n' for j in range(matelem)])
    nsplited = ndiag.split('\n')
    return '\n'.join([nsplited[i][::-1] for i in range(matelem)])

print rot_90_clock(s)
print '\n' + '\n'

def selfie_and_diag1(s):
    splited = s.split('\n')
    matelem = len(splited)
    elemlen = len(splited[0])
    diag1 = diag_1_sym(s)
    diag2 = diag1.split('\n')
    return '\n'.join([splited[i] + '|' + diag2[i] for i in range(matelem)])

print selfie_and_diag1(s)

def oper(fct, s):
    return fct(s)

############################
rot_90_clock = lambda s: zip(*s[::-1])
diag_1_sym = lambda s: zip(*s)
selfie_and_diag1 = lambda s: (tuple(l + '|') + r for l, r in zip(s, diag_1_sym(s)))
oper = lambda func, s: '\n'.join(map(''.join, func(s.split('\n'))))
