t = input()
s = t[::-1]
if hash(t) == hash(s):
    print(1)
else:
    print(0)