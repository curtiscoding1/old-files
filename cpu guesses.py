import random
print("think of a number between 1 and 100")

bottomlimit = 0
upperlimit = 100
def guess_num(bottomlimit,upperlimit):
    cpuguess = random.randint(bottomlimit,upperlimit)
    return cpuguess


lowestguess = 1
highestguess = 100
cpuguess = guess_num(1,100)
correct = 0


while correct == 0:
    eval = input(f'the cpu guessed {str(cpuguess)}, is this h(igh), l(ow) or e(xact)?')
    if eval == "l":
        lowestguess = cpuguess
        cpuguess = guess_num(lowestguess,highestguess)
    if eval == "h":
        highestguess = cpuguess
        cpuguess = guess_num(lowestguess,highestguess)
    if eval == "e":
        correct = 1
        print("the computer defeated the person >:)")