def thrandf(n):
    eq = 0
    while True:
        if eq % 3 == 0 and eq % 4 == 0:
            yield eq
        if eq == n:
            break
        else:
            eq+=1
        
    
    
n = int(input())

print(*thrandf(n))