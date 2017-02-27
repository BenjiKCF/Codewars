# Strings that start with the letters b, f, or k are naughty. Strings that start with the letters g, s, or n are nice

def whatListAmIOn(actions):
    a = [words[0] for words in actions]
    counting_list = []
    for char in a:
        if char == 'b' or char == 'f' or char == 'k':
            counting_list.append(1)
        elif char == 'g' or char == 's' or char == 'n':
            counting_list.append(2)
    if counting_list.count(1) >= counting_list.count(2):
        return 'naughty'
    else:
        return 'nice'


actions = ['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']

print whatListAmIOn(actions)

def whatListAmIOn(actions):
    nice,naut = 0,0
    for item in actions:
        if item.startswith(('b','f','k')):
            nice += 1
        elif item.startswith(('g','s','n')):
            naut += 1
    return 'nice' if nice < naut else 'naughty' 
