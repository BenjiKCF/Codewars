def countBits(n):
    return str(bin(n)[2:]).count("1")

print countBits(1234)#, 0);
