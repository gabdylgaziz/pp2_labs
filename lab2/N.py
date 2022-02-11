arr = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        arr.append(n)
while arr:
    if len(arr) != 1:
        print(arr[0] + arr[-1], end=' ')
        arr.pop(0)
        arr.pop(-1)
    else:
        print(arr[0], end=' ')
        arr.pop(0)
    