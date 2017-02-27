def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        T = -float(g) / (float(v1) - float(v2))
        m, s = divmod(T * 3600, 60)
        h, m = divmod(T * 60, 60)
        return [int(h), int(m), int(s)]

print race(720, 850, 70)
print race(80, 91, 37)
