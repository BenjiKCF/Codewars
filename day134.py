def rental_car_cost(d):
    if d >= 7:
        return d * 40 - 50
    if 3 <= d <= 7:
        return d * 40 - 20
    else:
        return d*40

print rental_car_cost(1)#,40)
