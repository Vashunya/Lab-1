import re

text1 = 'abbb ab aaaab aaa aa abb b bbb'

pattern = r"ab{2,3}"

result = re.finditer(pattern, text1)

for i in result:
    print(i)