arr = []

def dates(n):
    return n[2], n[1], n[0]

while True:
    n = input().split()
    if n[0] == '0':
        break
    arr.append(n)
#print(*arr)

arr.sort(key=dates)

for i in arr:
    print(*i)
