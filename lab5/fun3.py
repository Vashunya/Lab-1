import re

text1 = "hello_world hello world hi_kbtu"

pattern = r"[a-z]+_[a-z]+"

result = re.finditer(pattern, text1)

for i in result:
    print(i)