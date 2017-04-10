def decodeMorse(morseCode):
    import re
    codex = {'.-' : 'a', '-...':'b', '-.-.':'c', '-..':'d','.':'e','..-.':'f','--.':'g',
    '....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m', '-.':'n', '---':'o', '.--.':'p',
    '--.-':'q', '.-.':'r', '...':'s', '-':'t', '..-':'u', '...-':'v', '.--':'w', '-..-':'x',
    '-.--':'y', '--..':'z', '.----':'1', '..---':'2', '...--':'3', '....-':'4',
    '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0', '': ' ',
    '...---...':'sos', '-.-.--':'!', '.-.-.-':'.'}
    sentence = re.sub(' +', ' ', ''.join([codex[ch].upper() for ch in morseCode.split(' ')]))
    if sentence[0] == ' ':
        sentence = sentence[1:]
        if sentence[-1] == ' ':
            sentence = sentence[:-1]
    return sentence

print decodeMorse('.... . -.--   .--- ..- -.. .')

def decodeMorse(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))
