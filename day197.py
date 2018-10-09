def valid_parentheses(string):
    new_bracket = []
    for i in string:
        if i.isalpha():
            pass
        else:
            new_bracket.append(i)
    new_bracket = ''.join(new_bracket)

    while '()' in new_bracket:
        new_bracket = new_bracket.replace('()', '')
    return new_bracket==''

print valid_parentheses("hi(hi)()")# ,True)

# while '{}' in s or '()' in s or '[]' in s:
