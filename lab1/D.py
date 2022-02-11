byte = int(input())
type = input()
if(type == 'k'):
    after = input()
    b = "{:." + after + "f}"
    #byte = round(byte / 1024, after)
    #print(round(byte / 1024, after))
    print(b.format(byte / 1024))
    
else:
    print(byte * 1024)