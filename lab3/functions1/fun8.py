def spy_game(nums):
    goal = [0,0,7]
    check = 0
    programm_res = False
    for i in nums:
        if i == goal[check]:
            check+=1
        if check == len(goal):
            programm_res = True
            break
    return programm_res
    

print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # True
print(spy_game([1, 0, 2, 4, 0, 5, 7]))  # True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # False