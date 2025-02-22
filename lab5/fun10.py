import re

text = "HelloWorldHiKbtu"

pattern = r"([a-z])([A-Z])"

result = re.sub(pattern, lambda x: x.group(1) + "_" + x.group(2).lower(), text)

print(result)