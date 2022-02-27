def evens(n):
    eq = 0
    while True:
        if (eq % 2) == 0:
            yield eq
        if eq == n:
            break
        else:
            eq+=1
        
    
    
n = int(input())

print(*evens(n), sep=', ')
# 5
# 0, 2, 4