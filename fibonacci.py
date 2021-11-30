fiblength = int(input("how long do u want the fibonacci list to be?"))

fib = [1]
if fiblength == 1:
    pass
if fiblength == 2:
    fib = [1,1]
if fiblength > 2:
    fib = [1,1]
    for x in range (2,fiblength):
        fib.append(fib[x-1]+fib[x-2])

print(fib)



