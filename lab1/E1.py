dist, cart = map(int, input().split())

def isPrime(dist):
    for i in range(2, int(dist**0.5)+1):
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
    
        
        
    