import re

with open(r'/Users/vashunya/Desktop/tets1/lab5/row.txt', 'r') as file:
    text = file.read()

pattern = r"ab*"

result = re.finditer(pattern, text)

for i in result:
    print(i)