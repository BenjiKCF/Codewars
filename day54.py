import operator

def basic_op(operator1, value1, value2):
    op = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, '/' : operator.div, '%' : operator.mod, '^' : operator.xor}
    return op[operator1](value1, value2)

print basic_op('+', 4, 7) # 11

def basic_op(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))
