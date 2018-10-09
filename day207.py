def narcissistic( value ):
    num = 0
    for i in str(value):
        #print i
        #print len(str(value))
        num += int(i)**len(str(value))

    return num == value

print narcissistic(153)#, False, '122 is not narcissistic')
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))
