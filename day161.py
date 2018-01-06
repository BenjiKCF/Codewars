s = "abcd\nefgh\nijkl\nmnop"

def vert_mirror(strng):
    return '\n'.join([ch[::-1] for ch in strng.split('\n')])

def hor_mirror(strng):
    return '\n'.join([ch for ch in strng.split('\n')[::-1]])

def oper(fct, s):
    if fct == vert_mirror:
        return vert_mirror(s)
    elif fct == hor_mirror:
        return hor_mirror(s)

# print vert_mirror(s) #=> "dcba\nhgfe\nlkji\nponm"
#print hor_mirror(s) #=> "mnop\nijkl\nefgh\nabcd"
#print oper(vert_mirror, s)# => "dcba\nhgfe\nlkji\nponm"
#print oper(hor_mirror, s) #=> "mnop\nijkl\nefgh\nabcd"
def oper(fct, s):
    return fct(s)
