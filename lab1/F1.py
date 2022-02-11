n = int(input())

for i in range(n):
    line = int(input())
    if(line <= 10):
        print("Go to work!")
    else:
        if(line > 10 and line <= 25):
            print("You are weak")
        else:
            if(line > 25 and line <= 45):
                print("Okay, fine")
            else:
                print("Burn! Burn! Burn Young!")
    