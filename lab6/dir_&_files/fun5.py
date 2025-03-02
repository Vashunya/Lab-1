array = [1, 2, 3, 4, 5]

with open("fun5_res.txt", "w") as file:
    for item in array:
        file.write(f"{item}" + " ")