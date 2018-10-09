def get_towndata(town, strng):
    for line in strng.split('\n'):
        s_town, s_data = line.split(':')
        if s_town == town:
            return [s.split(' ') for s in s_data.split(',')]
    return None

def mean(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        return sum([float(x) for m,x in data]) / len(data)
    else:
        return -1.

def variance(town, strng):
    data = get_towndata(town, strng)
    if data is not None:
        mean = sum([float(x) for m,x in data]) / len(data)
        return sum([(float(x)-mean)**2 for m,x in data]) / len(data)
    else:
        return -1.
