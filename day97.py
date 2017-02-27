def stringy(size):
    string = []
    for i in range(size):
        if i % 2 == 0:
            string.append('1')
        else:
            string.append('0')
    return ''.join(string)



print stringy(10)# [0]#,'1',"Whoops your string doesn't start with a '1'")

def stringy(size):
    return "10" * (size / 2) + "1" * (size % 2)
