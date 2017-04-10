def validate_pin(pin):
    if (len(pin)==6 or len(pin)==4) and pin.isdigit():
        return True
    else:
        return False


print validate_pin("1234")# == True
print validate_pin("12345")# == False
print validate_pin("a234")# == False

def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
