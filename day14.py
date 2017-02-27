s1 = "This is a test!"
s2 = "hsi  etTi sats!"
s3 = "s eT ashi tist!"
s4 = " Tah itse sits!"

def decrypt(text, n):
    if n <=0:
        return text
    elif n == 1:
        return decrypt1(text)
    elif n > 1:
        return decrypt((decrypt1(text)), n-1)

def decrypt1(text):
    mid = len(text) / 2
    remainder = len(text) % 2
    lefthalf = text[:mid]
    righthalf = text[mid:]
    i = 0
    words = []
    while i < mid:
        nword = righthalf[i] + lefthalf[i]
        words.append(nword)
        i = i + 1
    words = ''.join(words)

    if remainder == 0:
        return words
    else:
        return words + righthalf[-remainder]


print decrypt(s4, 3)




def encrypt(text, n):
    if text == None or n <= 0:
        return text
    else:
        encrypted_text = text[1::2] + text[::2]
        i = 1
        while i < n:
            encrypted_text = encrypted_text[1::2] + encrypted_text[::2]
            i += 1
        return encrypted_text


print encrypt(s1, 1)


def decrypt(text, n):
    if text in ("", None):
        return text

    ndx = len(text) // 2

    for i in range(n):
        a = text[:ndx]
        b = text[ndx:]
        text = "".join(b[i:i+1] + a[i:i+1] for i in range(ndx + 1))
    return text



def encrypt(text, n):
    for i in range(n):
        text = text[1::2] + text[::2]
    return text
