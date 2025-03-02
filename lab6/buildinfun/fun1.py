array = [i for i in range(1, 11)]

for i in map(lambda x: x * x, array):
    print(i, end = " ")