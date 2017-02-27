def cat_mouse(x):
    return "Escaped!" if x.count('.') > 3 else "Caught!"


print cat_mouse('C....m')#, "Escaped!")
print cat_mouse('C..m')#, "Caught!")
