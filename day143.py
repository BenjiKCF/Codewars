def dont_give_me_five(start,end):
    return len([ch for ch in [str(i) for i in range(start, end+1)] if '5' not in ch])

print dont_give_me_five(1,9)#, 8
print dont_give_me_five(4,17)
