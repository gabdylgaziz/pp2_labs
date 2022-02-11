n = int(input())
arr = list(map(int, input().split()))
x = sorted(arr)
print(x[n - 1] * x[n - 2])