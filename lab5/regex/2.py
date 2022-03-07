import re 

pattern = 'ab{2,3}'

n = input()

print(bool(re.match(pattern, n)))