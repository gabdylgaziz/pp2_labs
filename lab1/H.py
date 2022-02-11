s = input()
letter = input()
size = list()

for i in range(len(s)):
    if(s[i] == letter):
        size.append(i)
n = len(size)
if(len(size) > 1):
    print(size[0], end=' ')
    print(size[n - 1])
else:
    print(*size)
    