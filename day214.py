def palindromization(elements, n):
    if elements == '' or n==1:
        return "Error!"

    elif n % 2 ==0:
        return pa_double(elements, n)
    else:
        return pa_single(elements, n)

def pa_double(elements, n):
    n = int(n)
    if n > len(elements)+1:
        return elements[:int(n/2)] + elements[:int(n/2%len(elements))] + elements[:int(n/2%len(elements))][::-1] + elements[:int(n/2)][::-1]
    else:
        return elements[:int(n/2)] + elements[:int(n/2)][::-1]

def pa_single(elements, n):
    n = int(n)
    if n > len(elements)+2:
        return elements[:int(n/2)] + elements[:int(n/2%len(elements))] + elements[int(n/2%len(elements))] + elements[:int(n/2%len(elements))][::-1] + elements[:int(n/2)][::-1]
    else:
        return elements[:int(n/2)] + elements[int(n/2)]+ elements[:int(n/2)][::-1]

def palindromization(elements, n):
    if not elements or n < 2: return "Error!"
    left = ((n // len(elements) + 1) * elements)[:(n + 1) // 2]
    return left + left[-1 - n % 2::-1]


#print palindromization("123",2)=="11"
#print palindromization("123",3)=="121"
#print palindromization("123",4)=="1221"
#print palindromization("123",5)=="12321"
#print palindromization("123",6)=="123321"
#print palindromization("123",7)=="1231321"
#print palindromization("123",8)=="12311321"
#print palindromization("123",9)=="123121321"
#print palindromization("123",10)=="1231221321"
# print palindromization("", )=="Error!"
