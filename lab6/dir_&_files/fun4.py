import os

with open(r"/Users/vashunya/Desktop/tets1/1.txt", "r") as fail:
    result = sum(1 for i in fail)

print("Number of lines in the file:", result)
