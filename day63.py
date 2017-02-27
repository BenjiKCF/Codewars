def count_red_beads(N_blue):
    return 0 if N_blue <= 1 else (N_blue -1) * 2


# X @@ X @@ X @@ X @@ X @@ X
print count_red_beads(0)#, 0)
print count_red_beads(1)#, 0)
print count_red_beads(3)#, 4)
print count_red_beads(5)#, 8)

def count_red_beads(nb):
    return max(0, 2 * (nb - 1) )
