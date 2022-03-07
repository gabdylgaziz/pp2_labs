import re 

pattern = 'a(0|[b+])'

n = input()

print(bool(re.match(pattern, n)))