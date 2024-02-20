#regex functions

import re

txt = "The rain in Spain"                            # returning list
x0 = re.findall("ai", txt)                           # find all "ai"'s in txt
print(x0)




txt = "The rain in Spain"                            # returning
x1 = re.search("\s", txt)                            # search for first space (its index)
print(x1.start())                    




txt = "The rain in Spain"                            #returning list
x = re.split("\s", txt, 1)                           #maxsplit = 1:    количество объектов для сплитов    
print(x)





txt = "The rain in Spain"                           
x = re.sub("\s", "9", txt, 2)                        #замена    (spaces -> "9")         
print(x)                                             #counter of substitutions = 2
