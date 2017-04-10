def remove(s):
    if s[-1] == '!':
        return remove(s[:-1])
    else:
        return s



print remove("Hi!")# == "Hi"
print remove("Hi!!!")# == "Hi"
print remove("!Hi")# === "!Hi"
print remove("!Hi!")# === "!Hi"
print remove("Hi! Hi!")# === "Hi! Hi"
print remove("Hi")# === "Hi"

def remove(s):
    return s.rstrip("!")
