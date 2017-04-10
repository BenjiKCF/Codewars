def replace_nth(text, n, old, new):
    if n <= 0:
        return text

    newstring = []
    occured = []
    newoccured = []

    for count, ch in enumerate(text):
        if ch == old:
            occured.append(count)

    if n >= len(occured)+1:
        return text
    else:
        for i in range(len(occured)):
            if (i+1) % n == 0:
                newoccured.append(occured[i])

    for i in range(len(text)):
        if i in newoccured:
            newstring.append(new)
        else:
            newstring.append(text[i])
    return ''.join(newstring)


#print replace_nth("Vader said: No, I am your father!", 2, 'a', 'o')
print replace_nth("Vader said: No, I am your father!", 4, 'a', 'o')
