from random import randint
digit = randint(1, 100)

while True:
    user_answer = (input("Guess the number or type Q to quit: "))
    if (user_answer) == "Q":
        print("Bye!")
        break
    elif int(user_answer) > digit:
        print('Too high!')
    elif int(user_answer) < digit:
        print('Too low!')
    else:
        print("You won!")
        break