def greet(name):
    return "Hello, my love!" if name == "Johnny" else "Hello, %s!" % name


print greet("James") # "Hello, James!")
print greet("Johnny")# "Hello, my love!")
