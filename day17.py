n = ()

def namelist(names):
    if len(names) > 1:
        return  ', '.join([names[i]['name'] for i in range(len(names)-1)]) + ' & ' + str(names[-1]['name'])
    elif len(names) == 1:
        return names[0]['name']
    else:
        return ''

print namelist(n)
