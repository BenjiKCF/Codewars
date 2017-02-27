def number(bus_stops):
    people = 0
    for k in range(len(bus_stops)):
        people = people + (bus_stops[k][0]) - (bus_stops[k][1])
    return people

print number([[10,0],[3,5],[5,8]])#,5)
#https://www.codewars.com/kata/number-of-people-in-the-bus/train/python

def number(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])
