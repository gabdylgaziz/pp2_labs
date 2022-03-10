import os

path = input()
papki = list()
faily = list()

os.chdir(path)

dirs = os.listdir(os.getcwd())
for i in dirs:
    if os.path.isdir(i):
        papki.append(i)
    elif os.path.isfile(i):
        faily.append(i)
print('<DIRS>: ', papki)
print('<FILES>: ',faily)
print('ALL: ')
for i in dirs:
    if os.path.isdir(i):
        print(f'<DIR> {i}')
    elif os.path.isfile(i):
        print(f'<FILE> {i}')