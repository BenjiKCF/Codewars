def reverse_slice(s):
    return [s[i::-1] for i in range(len(s))][::-1]


print reverse_slice('123')#, ['321', '21', '1'])
print reverse_slice('abcde')#, ['edcba', 'dcba', 'cba', 'ba', 'a'])
