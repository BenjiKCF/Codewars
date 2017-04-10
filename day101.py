def areYouPlayingBanjo(name):
    return ('%s plays banjo' % name) if name[0] in 'Rr' else ('%s does not play banjo' % name)


print areYouPlayingBanjo("martin")#, "martin does not play banjo");

# name + "plays banjo" name + "does not play banjo"
