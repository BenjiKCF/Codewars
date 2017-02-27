def freq_seq(s, sep):
    list1 = [s.count(ch) for ch in s]
    str1 = '%s'%sep.join(str(i) for i in list1)
    return str1


print freq_seq('hello world', '-') # 1-1-3-3-2-1-1-2-1-3-1

def freq_seq(s, sep):
    return sep.join([str(s.count(i)) for i in s])




def freq_seq1(s, sep):
    str1 = sep.join(str(s.count(i)) for i in s)
    return str1

print freq_seq1('hello world', '-')
