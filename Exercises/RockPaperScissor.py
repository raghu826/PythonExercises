from random import randint

choice = ['rock', 'paper', 'scissor']

for i in range(50):
    computer = choice[randint(0, 2)]
    select = input("rock or paper or scissor?")
    if select == computer:
        print("tie")
    else:
        if select == "rock":
            if computer == "paper":
                print("You lose!", computer, "covers", select)
            else:
                print("You win!", select, "smashes", computer)
        elif select == "paper":
            if computer == "scissor":
                print("You lose!", computer, "cut", select)
            else:
                print("You win!", select, "covers", computer)
        elif select == "scissor":
            if computer == "rock":
                print("You lose...", computer, "smashes", select)
            else:
                print("You win!", select, "cut", computer)
    if select not in choice:
        print("check spelling")









