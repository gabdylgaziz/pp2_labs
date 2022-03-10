import os
path = input()
try:
    os.chdir(path)
    txt = input()
    try: 
        output = open(txt, 'r')
        #cnt = len(output.readlines())
        #print('Количество строк: ', cnt)
        count = 0
        for line in output:
            if line != "\n":
                count += 1
        print('Количество строк:',count)
    except Exception as e:
        print(e)
        
except Exception as e:
    print(e)