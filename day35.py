def delete_nth(order,max_e):
    return [order.count(char) for char in order]


print delete_nth ([20,37,20,21],1) # return [20,37,21]
