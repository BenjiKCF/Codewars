def how_much_i_love_you(nb_petals):
    if nb_petals < 6:
        return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][nb_petals -1]
    else:
        return ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all'][nb_petals % 6 -1]
print how_much_i_love_you(3)
