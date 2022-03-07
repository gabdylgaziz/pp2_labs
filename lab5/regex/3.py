import re

seq = '[a-z_]+' 

arr = re.findall(seq, input())
if arr:
    print(*arr, sep='\n')