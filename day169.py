def procedure(i):
    timer = 2
    num = i
    num_list = [i]
    while num < 100:
        num = i * timer
        if num <= 100:
            num_list.append(num)
        timer += 1

    num_list = map(str, num_list)

    return sum([sum(map(int, i[:])) for i in num_list])



# print procedure(25)
print procedure(30)

def procedure(i):
    return sum(sum(int(d) for d in str(dd)) for dd in list(range(i, 101, i)))
    
