import re

text = "HelloWorldHiKbtu"

pattern = r"([a-z])([A-Z])"

result = re.sub(pattern, r"\1 \2", text)

print(result)