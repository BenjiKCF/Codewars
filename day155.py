def lovefunc( flower1, flower2 ):
    if flower1 % 2 != flower2 % 2:
        return True
    else:
        return False

print lovefunc(1,4)#, True)

def lovefunc(flower1, flower2):
    return flower1 % 2 != flower2 % 2

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
