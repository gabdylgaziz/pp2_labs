n = int(input())

compensations = {}

for i in range(n):
    name, money = input().split()
    if name not in compensations:
        compensations[name]= int(money)
    else:
        compensations[name]= int(money) + int(compensations[name]) 

#print(compensations.values())
x = max(compensations.values())
s = sorted(compensations.keys())
for i in s:
    if compensations[i] == x:
        print(i, "is lucky!")
    else:
        print(i, "has to receive", x - int(compensations[i]), "tenge")