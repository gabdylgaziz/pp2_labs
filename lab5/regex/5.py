import re

seq = '^a.*b$' 

print(bool(re.match(seq, input())))