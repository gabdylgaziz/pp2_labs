arr = list(map(int, input().split()))

def filter_prime(arr):
    if arr == 1 or arr == 0:
        return False
    for i in range(2, int(arr**0.5 + 1)):
        if arr % i == 0:
            return False
    return True
        

for i in range(len(arr)):
    if(filter_prime(arr[i])):
        print(arr[i], end=' ')
