ts = [50, 55, 56, 57, 58]

def choose_best_sum(t, k, ls):
    ts0 = ts
    ts1 = ts0.pop(0)
    ts0.append(ts1)

    ts2 = ts0
    ts3 = ts2.pop(0)
    ts2.append(ts3)
    return map(lambda x, y, z: x + y + z, ts, ts0, ts2)



print choose_best_sum(163, 3, ts)
