def fun(n):
    for i in range(1, n + 1):
        yield i*i

gen = fun(5)
print(next(gen))
print(next(gen))
print(next(gen))
