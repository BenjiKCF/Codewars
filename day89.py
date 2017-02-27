from fractions import Fraction
def mixed_fraction(s):
    n = s.split('/')
    num = int(n[0])
    den = int(n[1])
    if num < 0 and den > 0:
        num = -num
        whole_part = num // den
        fract_part = num % den
        s =Fraction(fract_part, den)
        if s == 0:
            return ("-{}".format(whole_part))
        elif whole_part == 0:
            return ("-{}".format(s))
        else:
            return ("-{} {}".format(whole_part, s))

    elif num > 0 and den < 0:
        den = -den
        whole_part = num // den
        fract_part = num % den
        s =Fraction(fract_part, den)
        if s == 0:
            return ("-{}".format(whole_part))
        elif whole_part == 0:
            return ("-{}".format(s))
        else:
            return ("-{} {}".format(whole_part, s))

    else:
        whole_part = num // den
        fract_part = num % den
        s =Fraction(fract_part, den)
        if s == 0:
            return ("{}".format(whole_part))
        elif whole_part == 0:
            return ("{}".format(s))
        else:
            return ("{} {}".format(whole_part, s))

print mixed_fraction('42/9')#, '4 2/3')
print mixed_fraction('6/3')
print mixed_fraction('-10/7')#, '-1 3/7')
print mixed_fraction('-22/-7')
print mixed_fraction('3685996/-3685996')
print mixed_fraction(0, 0)

from fractions import gcd





from fractions import Fraction

def mixed_fraction(s):
    f = Fraction(*map(int, s.split('/')))
    if f.denominator == 1: return str(f.numerator)
    n = abs(f.numerator) / f.denominator * (1 if f.numerator > 0 else -1)
    f = abs(f - n) if n else f - n
    return "{} {}".format(n, f) if n else str(f)
