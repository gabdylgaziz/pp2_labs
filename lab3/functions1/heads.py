numheads, numlegs = map(int, input().split())

def solve(numheads, numlegs):
    i = 1
    while True:
        if 4 * i + (numheads - i) * 2 == numlegs:
            return i, numheads - i
        i+=1
    

print(*solve(numheads, numlegs))