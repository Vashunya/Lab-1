def filter_prime(array):
    result = []
    for i in array:
        check = True
        if i < 2:
            continue
        for j in range(2, int(i**0.5) + 1):
            if(i % j == 0):
                check = False
                break
        if(check):
            result.append(i)
    return result

print(filter_prime([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))