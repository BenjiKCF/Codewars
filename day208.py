a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']

def in_array(array1, array2):
    result =[]
    for i in array1:
        for j in array2:
            if i in j:
                if i not in result:
                    result.append(i)
    return sorted(result)
print in_array(a1, a2)#, r)

def in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})
