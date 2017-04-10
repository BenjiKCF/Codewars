def maskify(cc):
    return str((len(cc)-4) *'#') + cc[-4:]

#def maskify(cc):
#    return "#"*(len(cc)-4) + cc[-4:]


print maskify("4556364607935616")# == "############5616"
print maskify(               "1")# ==                "1"
print maskify(               "21")# ==                "1"
print maskify(               "321")# ==                "1"
print maskify(               "4321")# ==                "1"
print maskify(               "54321")# ==                "1"
print maskify("Nananananananananananananananana Batman!") == "####################################man!"
