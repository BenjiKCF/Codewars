x = [0.0, 0.19, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.25]
s = 15


def gps(s, x):
    #  - x[0] + x[1], - x[1] + x[2]
    if len(x) <= 1:
        return 0
    else:
        dis = [(-x[i] + x[i+1]) for i in range(len(x)-1)]
        speed = map(lambda x: x/(float(s)/float(3600)), dis)
        return int(max(speed))

print gps(s,x)
