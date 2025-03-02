s = input()

up = sum(1 for i in s if i.isupper())
low = sum(1 for i in s if i.islower())

print(f"Upper: {up}\nLower: {low}")