def nba_extrap(ppg, mpg):
    return round(float(ppg) / mpg * 48, 1)


print nba_extrap(12, 20)
