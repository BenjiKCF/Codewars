def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return range(x, x*n+1, x)


print count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
print count_by(2,5) #should return [2,4,6,8,10]
