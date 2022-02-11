x, y = map(int, input().split())
n = int(input())
arr = []

def sortSecond(x):
    return x[1] 

for i in range(n):
    a, b = map(int, input().split())
    u = ((a - x)**2 + (b - y)**2)**(0.5)
    arr.append(((a, b), u))

arr.sort(key=sortSecond)

for i in arr:
    print(*i[0])