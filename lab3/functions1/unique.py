arr = list(map(int, input().split()))

uniq = []

def unique(arr, uniq):
    if arr not in uniq:
        uniq.append(arr)
    
for i in range(len(arr)):
    unique(arr[i], uniq)
    
print(uniq)