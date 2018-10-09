def to_camel_case(text):
    text = a_remover(text)
    text = b_remover(text)
    return text


def a_remover(text):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if text[i] == '-':
            text[i+1] = str(text[i+1]).upper()
        else:
            new_text.append(text[i])
    return ''.join(new_text)

def b_remover(text):
    text = list(text)
    new_text = []
    for i in range(len(text)):
        if text[i] == '_':
            text[i+1] = str(text[i+1]).upper()
        else:
            new_text.append(text[i])
    return ''.join(new_text)


# returns "theStealthWarrior"
# print to_camel_case("the-stealth-warrior")
# print to_camel_case("the_stealth_warrior")

# returns "TheStealthWarrior"
# print to_camel_case("The_Stealth_Warrior")

def to_camel_case(s):
    return s[0] + s.title().translate(None, "-_")[1:] if s else s

s = "The_stealth_warrior"
print s.title().translate(None, "-_")[1:]
print s.title().replace('_', '')
# title() can automatically makes the first word of the string upper case
