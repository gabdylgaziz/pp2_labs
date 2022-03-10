import os
path = input()
try:
    os.chdir(path)
    txt = input()
    output = open(txt, 'w')
    output.write(str(list(map(int, input().split()))))
    output.close()
except Exception as e:
    print(e)
