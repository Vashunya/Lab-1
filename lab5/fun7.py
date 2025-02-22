import re

text = "Hello_world"

pattern = r"_([a-z])"

result = re.sub(pattern, lambda x: x.group(1).upper() , text)

print(result)