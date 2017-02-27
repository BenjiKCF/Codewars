def longest(words):
    return max(len(char) for char in words)

words = ['simple', 'is', 'better', 'than', 'complex']
def longest(words):
    return max(map(len, words))

print map(len, words)
print [len(char) for char in words]
