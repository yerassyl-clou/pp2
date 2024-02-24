import re

f = open("prac/lab5/row.txt", "r",encoding="utf8")
text = f.read()

pattern = r"Ст"

results = re.search(pattern, text)


print(results.string)


'''

"^" - начало
"$" - конец

"*" - 0+ повторений
"+" - 1+ повторений
"?" - 0or1 повторений
"{n}" - n повторений

"\S" - блок без пробелов

'''

