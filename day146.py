def duplicate_encode(word):
    return ''.join(['(' if word.lower().count(ch) == 1 else ')' for ch in word])



print duplicate_encode("din") == "((("
print duplicate_encode("recede") == "()()()"
print duplicate_encode("Success") == ")())())"
print duplicate_encode("(( @") == "))(("
print duplicate_encode(")())())")
