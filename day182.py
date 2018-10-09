def to24hourtime(hour, minute, period):
    # hour will always range from 1 to 12 (inclusive)
    # minute will always range from 0 to 59 (inclusive)
    # period will always be either "am" or "pm"
    if period == 'pm':
            hour_convert = str(hour+12)
    else:
        if len(str(hour)) == 1:
            hour_convert = str(0)+str(hour)
        else:
            hour_convert = str(hour)
    if len(str(minute)) == 1:
        minute_convert = str(0)+str(minute)
    else:
        minute_convert = str(minute)

    if hour_convert+minute_convert >= '2400':
        hour_convert = str(int(hour_convert) - 12)

    return hour_convert+minute_convert

print to24hourtime(1, 0, 'am')

def to24hourtime(hour, minute, period):
    return '%02d%02d' % (hour % 12 + 12 * (period == 'pm'), minute)
