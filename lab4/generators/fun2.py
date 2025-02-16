def fun(n):
    for i in range(1, n + 1):
        if i % 2 == 0: yield i
        else: continue

digit = int(input())
gen = fun(digit)
print(next(gen))
print(next(gen))
print(next(gen))