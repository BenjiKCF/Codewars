def calculate_years(principal, interest, tax, desired):
    year = 0
    while principal < desired:
        principal = principal * (1 + interest) - principal * interest * tax
        year += 1
    return year

print calculate_years(1000, 0.05, 0.18, 1100)#, 3)
print calculate_years(1000,0.01625,0.18,1200)#, 14)
