n = input().split()

arr = []

for i in n:
    if i not in arr:
        arr.append(i)

arr.sort()

print(len(arr))

symbols = [',', '!', '?']
for i in arr:
    for y in i:
        if y in symbols:
            continue
        else:
            print(y, end='')
    print()