def duplicate_count(text):
    d = {}
    count = 0
    for i in text.lower():
        if i not in d:
            d[i] = 0
        else:
            d[i] += 1
    for i in d:
        if d[i] != 0:
            count += 1
    return count

#print duplicate_count("abcde")#, 0)
print duplicate_count("abcdeaB")#, 1)

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
