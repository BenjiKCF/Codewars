# sea_sick("~")
# "No Problem", "Throw Up"

def sea_sick(sea):
    count = 0.00
    for i in range(len(sea)-1):
        for j in range(len(sea)):
            if i+1==j and sea[i] != sea[j]:
                count += 1
    if count / len(sea) > 0.2:
        return "Throw Up"
    else:
        return "No Problem"

print sea_sick("_~~~~~~~_~__~______~~__~~_~~")

def sea_sick(sea):
    return "Throw Up" if (sea.count("~_") + sea.count("_~")) > 0.2*len(sea) else "No Problem"

sea_sick=lambda s:["No Problem","Throw Up"][s.count('~_')+s.count('_~')>.2*len(s)]
