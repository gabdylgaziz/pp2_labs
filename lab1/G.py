n = int(input())

def todec(n):
    if(n == 0):
        return 0
    else:
        return (n % 10 + 2 * todec(n // 10))

print(todec(n))

