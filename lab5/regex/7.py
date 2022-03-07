import re

def caps(s):
    stringg = ''
    for i in range(len(s)):
        if s[i - 1] == '_':
            stringg+=s[i].upper()
        else:
            stringg+=s[i]
    return stringg

print(re.sub('_', '', caps(input())))