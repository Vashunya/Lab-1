lenght = int(input("The number of digits:"))
feb = [1, 1]
for i in range(1, lenght - 1):
    feb.append(feb[i - 1] + feb[i])

for i in range(0, lenght):
    print(feb[i])
print(sum(feb))