def create_phone_number(n):
    n = map(str, n)
    return '(%s) %s-%s'%(''.join(n[0:3]), ''.join(n[3:6]), ''.join(n[6:]))

print create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])#, "(123) 456-7890")

def create_phone_number(n):
  return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
