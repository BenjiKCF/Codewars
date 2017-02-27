def tail_swap(strings):
        a1 = [ch for ch in strings][0].split(':')[0]
        b1 = [ch for ch in strings][1].split(':')[0]
        a2 = [ch for ch in strings][0].split(':')[1]
        b2 = [ch for ch in strings][1].split(':')[1]
        return [':'.join((a1, b2)), ':'.join((b1, a2))]
print tail_swap(['abc:123', 'cde:456']) #== ['abc:456', 'cde:123']
print tail_swap(['a:12345', '777:xyz']) #== ['a:xyz', '777:12345']

def tail_swap(arr):
    fmt = '{}:{}'.format
    (head, tail), (head_2, tail_2) = (a.split(':') for a in arr)
    return [fmt(head, tail_2), fmt(head_2, tail)]
