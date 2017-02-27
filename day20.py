def title_case(title, minor_words=''):
    minor_words = minor_words.lower().split()
    result = []
    for i,word in enumerate(title.split()):
        if word.lower() in minor_words and i != 0:
            result.append(word.lower())
        else:
            result.append(word.title())
    return ' '.join(result)

print title_case('a clash of KINGS', 'a an the of')
print title_case('THE WIND IN THE WILLOWS', 'The In')

#A Clash of Kings

def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])

print title_case('a clash of KINGS', 'a an the of')
print title_case('THE WIND IN THE WILLOWS', 'The In')
