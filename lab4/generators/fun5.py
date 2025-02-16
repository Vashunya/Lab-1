def fun(a):
    for i in range(a, 0, -1):
        yield i

gen = fun(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))