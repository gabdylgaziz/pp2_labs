dist, cart = map(int, input().split())

def isPrime(dist):
    if dist == 2 or dist == 3: return True
    if dist % 2==0 or dist < 2: return False
    for i in range(3, int(dist**0.5)+1, 2):
        if dist % i == 0:
            return False    

    return True

if(dist > 500):
    print("Try next time!")
else:
    if(isPrime(dist) and cart % 2 == 0):
        print("Good job!")
    else:
        print("Try next time!")
    
        
        
    