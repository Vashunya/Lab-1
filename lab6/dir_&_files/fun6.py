import string, os

os.mkdir("for_fun6")

for letter in string.ascii_uppercase:
    with open(os.path.join("for_fun6", letter + ".txt"), "w") as f:
        f.writelines(letter)