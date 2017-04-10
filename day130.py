def xor(a,b):
    return bool(a) != bool(b)


print xor(False, False)#, False, "False xor False == False")
print xor(True, False)#, True, "True xor False == True")
print xor(False, True)#, True, "False xor True == True")
print xor(True, True)#, False, "True xor True == False")
