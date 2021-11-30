wordinput = input("what word do you want to use? ")



def reversal (word):
    wordlength = len(word)
    n = wordlength - 1
    reversed_word = ""
    while n >= 0:
        reversed_word = reversed_word + word[n]
        n = n - 1
    return reversed_word


if wordinput == reversal(wordinput):
    print("this is a palindrome")
else:
    print("not a palindrome")
