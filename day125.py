def how_much_i_love_you(nb_petals):
    return ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 -1]

print how_much_i_love_you(7)#,"I love you")
print how_much_i_love_you(3)#,"a lot")
print how_much_i_love_you(6)#,"not at all")
