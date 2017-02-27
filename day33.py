# (5.00, 5, 10), 5.75

def calculate_total(subtotal, tax, tip):
    return round(subtotal * (1 + tax/100.00) + subtotal * (tip/100.00),2)



print calculate_total(36.97, 7, 15)
