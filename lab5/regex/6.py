import re
s = input()
pattern = r'[ ,:]'
l = list(re.split(pattern, s))
print(*l)