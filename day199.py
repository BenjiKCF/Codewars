def spin_words(sentence):
    return ' '.join([i[::-1] if len(i) >=5 else i for i in sentence.split(' ')])


#print spin_words("Welcome")#, "emocleW")
print spin_words( "Hey fellow warriors" )
