def decode(s):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return [alpha[i-1] for i in s]


s = [13, 5, 18, 15, 4, 6]
print decode(s)

6 18 5 5 4 15 13
