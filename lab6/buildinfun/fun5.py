s = input()
array = tuple(map(int, s.split(" ")))
if all(array) == True:
    print("True")
else:
    print("False")