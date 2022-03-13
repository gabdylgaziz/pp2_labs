import os
path = input()
try:
    os.chdir(path)
    name = input()
    print("Существует:", os.access(name, os.F_OK))
    print("Доступен на чтение:", os.access(name, os.R_OK))
    print("Доступен на запись:", os.access(name, os.W_OK))
    print("Доступен на исполнение:", os.access(name, os.X_OK))
except Exception as e:
    print(e)