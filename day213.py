def goodVsEvil(good, evil):

    good = map(int, good.split(' '))
    evil = map(int, evil.split(' '))

    goodd = [1, 2, 3, 3, 4, 10]
    evild = [1, 2, 2, 2, 3, 5, 10]

    sumgood = 0
    sumevil = 0
    for i, goodi in enumerate(good):
        sumgood += goodi * goodd[i]

    for i, evili in enumerate(evil):
        sumevil += evili * evild[i]

    if sumgood > sumevil:
        return "Battle Result: Good triumphs over Evil"
    elif sumevil > sumgood:
        return "Battle Result: Evil eradicates all trace of Good"
    elif sumevil == sumgood:
        return "Battle Result: No victor on this battle field"


#print goodVsEvil('1 1 1 1 1 1', '1 1 1 1 1 1 1')#,  'Battle Result: Evil eradicates all trace of Good', 'Evil should win')
print goodVsEvil('0 0 0 0 0 10', '0 1 1 1 1 0 0')
