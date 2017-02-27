demo = ("22 33 56 2 1.4 67.4 34.5 49 11.2")

# Make it into a list
# split the space and add comma
# Make the string into a floating number
values = [float(i) for i in demo.split()]
print sum(float(i) for i in values)
