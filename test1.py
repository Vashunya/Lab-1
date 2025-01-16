def mix(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1 = set()
    list2 = set()
    dict1 = {}
    dict2 = {}
    for i in list1:
        if i.isalpha() and i.islower():
            dict1[i] += 1
    for i in list2:
        if i.isalpha() and i.islower():
            dict2[i] += 1
    list1.append(list2)
    list1 = set()
    result = ""
    for i in list1:
        if dict1[i] > 1 or dict2[i] > 1:
            if dict1[i] > dict2[i]:
                result += f"1:{i*dict1[i]}"
            elif dict1[i] < dict2[i]:
                result += f"2:{i*dict2[i]}"
            else:
                result += f"=:{i*dict1[i]}"
        else: continue
    return result
