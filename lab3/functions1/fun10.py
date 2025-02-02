def unique_list(array):
    result = []
    for i in array:
        if i in result:
            continue
        else: result.append(i)
    return result

print(unique_list([1,1,2,4,3,4]))