n = int(input())
arr = []

for i in range(n):
    s = input()
    low = 0
    up = 0
    dig = 0
    for ind in s:
        if ind.islower():
            low = 1
            break
        else:
            continue
    for ind in s:
        if ind.isupper():
            up = 1
            break
        else:
            continue
    for ind in s:
        if ind.isdigit():
            dig = 1
            break
        else:
            continue
    if low == 1 and up == 1 and dig == 1 and s not in arr:
        arr.append(s)
        
arr.sort()
print(len(arr))
for i in arr:
    print(i)
















