import re

seq = '[A-Z][a-z]+' 

arr = re.findall(seq, input())
if arr:
    print(*arr, sep='\n')