def knight_or_knave(says):
    if bool(says) == True:
        return 'Knight!'
    elif bool(says) == False:
        return 'Knave! Do not trust.'

print knight_or_knave(True)
print knight_or_knave(False)
print knight_or_knave(True and False)
print knight_or_knave(True or False)
print knight_or_knave(not False and True or False or True )
print knight_or_knave('2+2==4')
print knight_or_knave('false')
