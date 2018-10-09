def century(year):
    if year/100 % 1 != 0:
        return int(year/100) + 1
    else:
        return year/100

print century(1900)#, 19, 'Testing for year 1900')
print century(2000)#, 20, 'Testing for year 2000')

def century(year):
    return (year + 99) // 100
