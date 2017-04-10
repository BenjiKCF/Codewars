def filter_list(l):
    return [ch for ch in l if type(ch) == int]




print filter_list([1,2,'a','b'])#,[1,2])
print filter_list([1,2,'aasf','1','123',123])#,[1,2,123])
