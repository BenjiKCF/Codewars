def get_middle(s):
    if len(s) % 2 != 0:
        return s[len(s)/2]
    else:
        return s[len(s)/2 -1 : len(s)/2 + 1]

def get_middle(s):
    return s[len(s)/2] if len(s) % 2 != 0 else s[len(s)/2 -1 : len(s)/2 + 1]


print get_middle("test")#,"es")

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
