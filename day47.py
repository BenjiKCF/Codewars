def solution(items, index, default_value):
    for i in range(len(items)):
        if items[i] == None:
            return None
        elif index > 0 and index <= len(items) or index < 0 and -index <= len(items):
            return items[index]
        else:
            return default_value


data = ['a', 'b', 'c']
print solution(data, 1, 'd') # should == 'b'
print solution(data, 5, 'd') # should == 'd'
print solution(data, -1, 'd') # should == 'c'
print solution(data, -5, 'd') # should == 'd'

def solution(items, index, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value
