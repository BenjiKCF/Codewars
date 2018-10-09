from os import listdir
from os.path import isfile, join
from datetime import date

mypath = '/Users/kachunfung/python/codewars/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

py_removed = [i.replace('.py','') for i in onlyfiles]
file_counter_removed = py_removed.remove('file_counter')
day_removed = max([int(j.replace('day','')) for j in py_removed])

d0 = date(2016, 11, 7)
d1 = date.today()
delta = d1 - d0

if day_removed >= delta.days:
    print "Well done!\nYou are %s days ahead.\nKeep up the good work! I am proud of you." % (day_removed - delta.days)
else:
    print "You are %s days behind schedule.\nTry your best and Never give up!" % (delta.days - day_removed)
print "\nYou have completed %s codewars kata since 7th December 2016" % day_removed
