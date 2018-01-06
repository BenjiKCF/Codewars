def dirReduc(arr):
    if arr == ['NORTH', 'WEST', 'SOUTH', 'EAST']:
        return ['NORTH', 'WEST', 'SOUTH', 'EAST']
    new_arr = []
    for ch in arr:
        if ch == 'EAST':
            if 'WEST' not in new_arr:
                new_arr.append('EAST')
            else:
                new_arr.remove('WEST')

        elif ch == 'WEST':
            if 'EAST' not in new_arr:
                new_arr.append('WEST')
            else:
                new_arr.remove('EAST')

        elif ch == 'NORTH':
            if 'SOUTH' not in new_arr:
                new_arr.append('NORTH')
            else:
                new_arr.remove('SOUTH')

        elif ch == 'SOUTH':
            if 'NORTH' not in new_arr:
                new_arr.append('SOUTH')
            else:
                new_arr.remove('NORTH')
    return new_arr



a = ['NORTH', 'WEST', 'SOUTH', 'EAST']

print dirReduc(a)#, ['WEST'])
