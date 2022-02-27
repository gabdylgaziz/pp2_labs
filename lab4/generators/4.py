def squares(a, b):
    sq = a
    while True:
        yield sq * sq
        if sq == b:
            break
        else:
            sq+=1
    
    
a, b = map(int, input().split())

print(*squares(a, b))