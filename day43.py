def prefill(n,v):
    if not v:
        return ['undefined' for i in range(n)]
    elif n == 0:
        return []
    elif not str(n).isdigit():
        return TypeError, '%s is invalid'%n
    elif str(n).isdigit():
        return [v for i in range(int(n))]
    else:
        return [v for i in range(n)]


print prefill(3,1) #[1,1,1]
print prefill(2,'abc')
print prefill('1', 1)
print prefill(3, prefill(2,'2d'))
print prefill('xyz', 1)
