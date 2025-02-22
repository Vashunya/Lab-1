import re

with open(r'/Users/vashunya/Desktop/tets1/lab5/row.txt', 'r') as file:
    text = file.read()

pattern = r"[A-Z]\w*"

result = re.findall(pattern, text)

print(result)