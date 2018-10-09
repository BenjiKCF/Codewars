def pig_it(text):
    text = text.split(' ')
    return ' '.join([word[1:]+word[0]+'ay' if word.isalpha() else word for word in text])

print pig_it('Pig latin is cool') # igPay atinlay siay oolcay
print pig_it('Hello world !')     # elloHay orldWay !
