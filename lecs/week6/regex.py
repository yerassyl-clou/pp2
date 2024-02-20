# [0-9] check for numbers from 1 to 9     (need to input re)
# [a-z]
# [A-Z]

import re                                                               # '^'	Starts with, '$'	Ends with
                                                                        
str = input()                                                           
pattern = r"^"                                                           # '\' - any number of objects, 'S' - any symbol without spaces

x = re.search(pattern, str)

print(x)