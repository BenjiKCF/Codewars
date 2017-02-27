costs = {'socks':5, 'shoes':60, 'sweater':30}
def getTotal(costs, items, tax):
    items1 = [ch for ch in items if ch in costs]
    return round(sum([costs[word] for word in items1])*(1+tax),2)

print getTotal(costs, ['socks', 'shoes'], 0.09)
print getTotal(costs, ['shirt', 'shoes'], 0.09)

#-> 5+60 = 65

#-> 65 + 0.09 of 65 = 70.85

#-> Output: 70.85

def getTotal(costs, items, tax):
    return round(sum(costs.get(e, 0) for e in items) * (1 + tax), 2)
