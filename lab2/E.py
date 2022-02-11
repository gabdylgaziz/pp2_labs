si = input().split()
if len(si) == 1:
    si = int(si[0])
    st = int(input())
else:
    si, st = int(si[0]), int(si[1])
xo = 0
for i in range(si):
    xo^=(st + 2*i)
print(xo)