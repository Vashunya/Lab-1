def fun(a, b):
    for i in range(a, b + 1):
        yield i*i

for j in fun(5, 10):
    print(j, end = " ")