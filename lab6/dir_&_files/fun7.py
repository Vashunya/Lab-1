with open(r"/Users/vashunya/Desktop/tets1/1.txt", "r") as file_for_copy:
    file = file_for_copy.read()

with open("1_1.txt", "w") as file_for_write:
    file_for_write.write(file)
