def validBraces(string):
    new_str = lefttoright(string)
    return middleoutchecker(new_str)

def lefttoright(string):
    brace_dict = {'(':')', '[':']', '{':'}'}
    brace_list = ['[', '(', '{']
    new_str = []
    for i in range(0,len(string),2):
        if string[i] in brace_list:
            try:
                if brace_dict[string[i]] == string[i+1]:
                    pass
                else:
                    new_str.append(string[i])
                    new_str.append(string[i+1])
            except:
                new_str.append(string[i])
                new_str.append(string[i+1])
        else:
            new_str.append(string[i])
            new_str.append(string[i+1])
    return ''.join(new_str)


def middleoutchecker(string):
    brace_dict = {'(':')', '[':']', '{':'}'}
    try:
        for i in range(len(string[:len(string) / 2])):
            if brace_dict[string[i]] == string[-(i+1)]:
                pass
            else:
                return False
        return True
    except:
        return False


def validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''


#print validBraces("()")
#print validBraces("([{}])")

#print validBraces("[({})](]")
#print validBraces("{}()[]")
#print validBraces("{}()[]")


print validBraces("{}[)(]")
#print validBraces("{}[()]")
