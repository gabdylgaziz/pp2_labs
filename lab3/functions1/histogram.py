arr = [4, 9, 7]

def histogram(arr):
    for i in arr:
        for y in range(i):
            print('*', end='')
        print('')
        
histogram(arr)

