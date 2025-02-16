import math
sides = int(input("sides: "))
lenght = int(input("len of side: "))

print(int((sides * lenght ** 2) / (4 * math.tan(math.pi / sides))))