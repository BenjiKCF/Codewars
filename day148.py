def order(sentence):
    sen = {}
    for word in sentence.split():
        for num in word:
            if num in map(str,[0,1,2,3,4,5,6,7,8,9]):
                    sen[num] = word
    wsen = []
    for i in sorted(sen):
        wsen.append(sen[i])
    return ' '.join(wsen)

print order("is2 Thi1s T4est 3a")#, "Thi1s is2 3a T4est")

def order(sentence):
    return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))
