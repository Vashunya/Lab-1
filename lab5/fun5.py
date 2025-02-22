import re

text = 'apfdsb aagf bbaaab aab ab'

pattern = r"a\S*b"

result = re.finditer(pattern, text)

for i in result:
    print(i)