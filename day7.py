def get_grade(s1, s2, s3):
    if (s1 + s2 + s3)/3 in range(90, 101):
        return "A"
    elif (s1 + s2 + s3)/3 in range(80, 91):
        return "B"
    elif (s1 + s2 + s3)/3 in range(70, 81):
        return "C"
    elif (s1 + s2 + s3)/3 in range(60, 71):
        return "D"
    else:
        return "F"

print get_grade(5, 90, 93)
