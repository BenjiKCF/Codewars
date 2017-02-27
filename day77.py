def calculate_grade(scores):
    avg = sum(scores)//len(scores)
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


print calculate_grade([92, 94, 99])#, "A")
print calculate_grade([52, 55])#, "F"
