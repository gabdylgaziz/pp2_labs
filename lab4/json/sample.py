import json as js

f = open('sample-data.json', 'r').read()
d = js.loads(f)

with open('output.json', 'w') as output:
    output.write('Interface Status' + '\n')
    output.write('================================================================================' + '\n')
    output.write('DN                                                 Description           Speed    MTU  ' + '\n')
    output.write('-------------------------------------------------- --------------------  ------  ------' + '\n')
    for i in range(len(d["imdata"])):
        if len(d['imdata'][i]['l1PhysIf']['attributes']['dn']) == 42:
            output.write(d['imdata'][i]['l1PhysIf']['attributes']['dn'] + '                              ' + d['imdata'][i]['l1PhysIf']['attributes']['fecMode'] + '   ' + d['imdata'][i]['l1PhysIf']['attributes']['mtu'] + '\n')
        else:
            output.write(d['imdata'][i]['l1PhysIf']['attributes']['dn'] + '                               ' + d['imdata'][i]['l1PhysIf']['attributes']['fecMode'] + '   ' + d['imdata'][i]['l1PhysIf']['attributes']['mtu'] + '\n')
        
    output.close()


