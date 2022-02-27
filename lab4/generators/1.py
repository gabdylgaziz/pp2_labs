def squares(n):
    sq = 0
    while True:
        yield sq * sq
        if sq == n:
            break
        else:
            sq+=1
    
    
n = int(input())

print(*squares(n))