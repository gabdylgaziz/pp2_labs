n = int(input())

def nums(n):
    number = n
    while number >= 0:
        yield number
        number-=1
    


print(*nums(n))