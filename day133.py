def bonus_time(salary, bonus):
    return '$%s'%(salary * 10) if bonus is True else '$%s'%salary


print bonus_time(25000, True)#, '$250000')
