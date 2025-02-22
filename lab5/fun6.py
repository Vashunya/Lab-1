import re

with open(r'/Users/vashunya/Desktop/tets1/lab5/row.txt', 'r') as file:
    text = file.read()

pattern = r"[ ,.]"

result = re.sub(pattern, ";", text)

print(result)