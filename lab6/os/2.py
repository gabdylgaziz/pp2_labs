import os
path = input()
try:
    os.chdir(path)
    print(os.getcwd())
except Exception as e:
    print(e)