def reversed():
    string = input()
    res = string.split()
    res.reverse()
    return " ".join(res)

print(reversed())