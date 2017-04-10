def remove(s):
    try:
        return s[:-1] if s[-1] == '!' else s
    except:
        return ''

def remove(s):
    return s[:-1] if s.endswith('!') else s


print remove("Hi!")# === "Hi"
print remove("Hi!!!")# === "Hi!!"
print remove("!Hi")# === "!Hi"
print remove("!Hi!")# === "!Hi"
print remove("Hi! Hi!")# === "Hi! Hi"
print remove("Hi")# === "Hi"
print remove('')
