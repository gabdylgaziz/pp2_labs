n = int(input())

arr = []

for i in range(n):
    u = input().split()
    if int(u[0]) == 1:
        arr.append(u[1])
    else:
        print(arr[0], end = " ")
        arr.pop(0)
