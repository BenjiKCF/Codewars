def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    c = {'scissors':'paper', 'paper':'rock', 'rock':'scissors'}
    if c[p1] == p2:
        return "Player 1 won!"
    else:
        return "Player 2 won!"

print rps('scissors','paper')
