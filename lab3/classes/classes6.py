prime = lambda array: array > 1 and all(array % j != 0 for j in range(2, int(array**0.5)+1))

print(list(filter(prime, [3, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])))