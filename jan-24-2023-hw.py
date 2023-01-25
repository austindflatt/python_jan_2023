import random
"""
Number guessing game problem 

System generates a random number 
user has to guess what number it is.
Write as a function

hint: use while loop and input(). 

"Welcome to the number guessing game"
"number generated" i.e. 4

guess: ---> 3 
"that's incorrect!"
guess: ---> 5
"that's incorrect"
guess: ---> 4
"that's correct"


"""
ans = random.randint(1,10)

guess = int(input("Enter any number: "))
while ans != guess:
    if guess < ans:
        print("too low")
        guess = int(input("Enter number again: "))
    elif guess > ans:
        print("too high")
        guess = int(input("Enter number again: "))
    else:
        break

print("that's correct")


"""
write a function that reverses the string without using [::-1]
(uses only looping)
"""


def reverse_string(s):
    reversed_string = ""
    for i in range(len(s) - 1, -1, -1):
        reversed_string += s[i]
    return reversed_string


print(reverse_string("hello"))