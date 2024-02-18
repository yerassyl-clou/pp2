import json

with open ('vscode/kbtu/pp2/labs/lab4/json/sample-data.json') as file:                                                                          #open json file
    data = json.load(file)

list = []                                                                                                                                       #list of final data

for item in data['imdata']:                                                                                                                     #loop all data in 'imdata'
    
    atr = item['l1PhysIf']['attributes']                                                                                                        #create atribute that will take data from attributes from l1Phys
    list.append({                               
        'dn': atr.get('dn'),
        'descr': atr.get('descr'),
        'speed': atr.get('speed'),
        'mtu': atr.get('mtu')
    })                                                                                                                                          #append data

txt = '''                                                                                           
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
'''                                                                                                     #space (↑↑↑)

print(txt)

for item in list:
    print(item['dn'], str(" " * int(55 - len(item['dn']))), item['descr'], str(" " * int(20 - len(item['speed']))), item['speed'], str(" " * int(5 - len(item['mtu']))), item['mtu'])