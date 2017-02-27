import re

def domain_name(url):
    if 'http://' in url:
        regex = 'http://(.+?).com'
        pattern = re.compile(regex)
        name = re.findall(pattern, url)
        name1 = ''.join(name)
        if 'www.' in name1:
            name1 = name1.strip('www.')
        return name1
    elif 'https://' in url:
        regex = 'https://(.+?).com'
        pattern = re.compile(regex)
        name = re.findall(pattern, url)
        name1 = ''.join(name)
        if 'www.' in name1:
            name1 = name1.strip('www.')
        return name1
    else:
        regex = '(.+?).ru'
        pattern = re.compile(regex)
        name = re.findall(pattern, url)
        name1 = ''.join(name)
        if 'www.' in name1:
            name1 = name1.strip('www.')
        return name1

print domain_name("http://github.com/carbonfive/raygun")
print domain_name("http://www.zombie-bites.com")
print domain_name("https://www.cnet.com")
print domain_name("https://www.codewars.com/kata/extract-the-domain-name-from-a-url-1/train/python")
print domain_name('www.xakep.ru')

def domain_name1(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

print domain_name1("http://github.com/carbonfive/raygun")
