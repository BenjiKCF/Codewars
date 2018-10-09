def move_zeros(array):
    n_array = []
    z_array = []
    for i in array:
        if (i == 0 or i==0.):#and i != False:
            if str(i) == str(False):
                n_array.append(i)
            else:
                z_array.append(i)
        else:
            n_array.append(i)
    return n_array + z_array

print move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9])#
# ['a', 'b', None, 'c', 'd', 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
