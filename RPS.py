import random

cpumove = random.randint(1,3)
again = 0
movelist = {"R": 1, "P": 2, "S": 3}
inverselist = {1: "Rock", 2: "Paper", 3: "Scissors"}

while again == 0:
    move = input("rock (R), paper (P) or scissors (S)")
    while move not in movelist:
        print("that isnt a move try again")
        move = input("rock (R), paper (P) or scissors (S)")
    if movelist[move] == cpumove:
        print(f"Draw! The CPU chose {inverselist[cpumove]}")
        more = input("play again? Y or N")
        if more == "N":
            again = 1

    elif movelist[move] == cpumove + 1:
        print(f"You Win! The CPU chose {inverselist[cpumove]}")
        more = input("play again? Y or N")
        if more == "N":
            again = 1

    elif movelist[move] == cpumove - 1 or cpumove + 2:
        print(f"You Lose! The CPU chose {inverselist[cpumove]}")
        more = input("play again? Y or N")
        if more == "N":
            again = 1


print ("Thanks for playing")