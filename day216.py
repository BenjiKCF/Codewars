def human_years_cat_years_dog_years(human_years):
    a = human_years
    b = 15
    c = 15
    if human_years > 1:
        b += 9
        c += 9
    for i in range(human_years - 2):
        b += 4
        c += 5
    return [a, b, c]
