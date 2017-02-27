lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']

def mean(lst):
    nlst = [float(i) for i in lst if i.isdigit() == True]
    alst = [x for x in lst if x.isdigit() != True]
    alst = ''.join(alst)
    return [sum(nlst)/10, str(alst)]


print mean(lst)

def mean(lst):
    return [sum(int(n) for n in lst if n.isdigit()) / 10.0, "".join(c for c in lst if c.isalpha())]
