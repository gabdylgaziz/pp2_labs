n = int(input())
mail = '@gmail.com'
for i in range(n):
    s = input()
    if s.endswith(mail):
        print(s[:-10])
    
    
    