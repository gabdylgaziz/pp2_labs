arr = list(map(int, input().split()))

def asmay(arr):
    endpos = len(arr) - 1
    for i in range(len(arr) - 2, -1, -1):
        if i + arr[i] >= endpos:
            endpos = i
    return endpos == 0


if asmay(arr) == True:
    print(1)
else:
    print(0)