import itertools

def string_permutations():
    string = input()
    for i in itertools.permutations(string):
        print(''.join(i))

string_permutations()