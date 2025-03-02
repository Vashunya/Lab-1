import os

if os.path.exists("/Users/vashunya/Desktop/tets1/1_1.txt"):
    os.remove("/Users/vashunya/Desktop/tets1/1_1.txt")
else:
    print("The file does not exist")