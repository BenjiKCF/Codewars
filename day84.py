def toJadenCase(string):
    return ' '.join(map(str.capitalize, string.split()))


quote = "How can mirrors be real if our eyes aren't real"
print toJadenCase(quote)#, "How Can Mirrors Be Real If Our Eyes Aren't Real")
