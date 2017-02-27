import re
def area_code(text):
    regex = '\((.+?)\)'
    pattern = re.compile(regex)
    code = re.findall(pattern, text)
    return ''.join(code)

print area_code("The supplier's phone number is (555) 867-5309") # '555'

def area_code(text):
  return text[text.index('(')+1:text.index(')')]

import re
def area_code(text):
    return re.search("\((\d{3})\)", text).group(1)
