import re
consonants = "qwrtypsdfghjklzxcvbnm"
vowels = "aeiou"
string = input()
expression = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (consonants, vowels, consonants), string, flags = re.I)

if expression:
    for i in expression:
        print(i)
else:
    print(-1)