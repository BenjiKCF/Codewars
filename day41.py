def take_umbrella(weather, rain_chance):
    if weather == 'rainy':
        return True
    elif weather == 'cloudy' and rain_chance > 0.20:
        return True
    elif weather == 'sunny' and rain_chance > 0.50:
        return True
    else:
        return False


print take_umbrella('sunny', 0.40)
# You should take an umbrella if it's currently raining or if it's cloudy and the chance of rain is over 0.20.

def take_umbrella(weather, rain_chance):
    return rain_chance > {'sunny': 0.5, 'cloudy': 0.2, 'rainy': -1}[weather]
