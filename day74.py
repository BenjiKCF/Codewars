import re

def nothing_special(s):
    try:
        return re.sub('[^a-z0-9\s]', '', s, flags=re.IGNORECASE)
    except:
        return 'Not a string!'

print nothing_special("Hello World!")#, "Hello World")
print nothing_special(25)
print nothing_special(25.0)
print nothing_special(9)
print nothing_special('benji2b5n5')
