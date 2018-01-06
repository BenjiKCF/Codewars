def remove(s):
    return s.replace('!', '') + '!'



print remove("Hi!")# === "Hi!"
print remove("Hi!!!")# === "Hi!"
print remove("!Hi") #=== "Hi!"
print remove("!Hi!") #=== "Hi!"
print remove("Hi! Hi!") #=== "Hi Hi!"
print remove("Hi") #=== "Hi!"
