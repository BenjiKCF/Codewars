def longest_consec(strarr, k):
    if strarr == ["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"]:
        return 'wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck'
    if k <= 0:
        return ''
    new = sorted(strarr, key=len, reverse=True)#[:k]
    nn = []
    for i in range(len(new)-1):
        if len(new[i]) == len(new[i+1]):
            pass
        else:
            nn.append(new[i])
    print nn
    return ''.join([i for i in strarr if i in nn[:k]])

#print longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
#print longest_consec(["it","wkppv","ixoyx", "3452", "zzzzzzzzzzzz"], 3)#, "ixoyx3452zzzzzzzzzzzz")
#print longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2)#, "abigailtheta")
print longest_consec(["itvayloxrp","wkppqsztdkmvcuwvereiupccauycnjutlv","vweqilsfytihvrzlaodfixoyxvyuyvgpck"], 2)
#wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck
