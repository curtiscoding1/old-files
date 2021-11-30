inputtednumber = int(input("wasurnumber?"))

def isitprime(number):
    nonprime = 0
    for x in range (2,number-1):
        if number % x == 0:
            print(f"we found a divisor, the number is {x}")
            nonprime = 1

    return nonprime

if isitprime(inputtednumber) == 1:
    print("its not prime")
else:
    print("its prime")

