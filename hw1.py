# 1. Write a function called char_lookup that takes a string and returns a character at a given index

def char_lookup(string, index):
    return string[index]


print("red"[1])
print("black"[1])
print("green"[-1])
print("blue"[-2])

# 2. Write a function that prints every second character of a given string


def every_second_char(string):
    return string[::2]


print(every_second_char("AaBbCcDd"))
print(every_second_char("HeEeLlLlOo"))

# 3. Write a function that reverses a given string using []


def reverse(string):
    return string[::-1]


print(reverse("abcd"))
print(reverse("hello"))

"""

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Input: n = 3
Output: ["1","2","Fizz"]

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""

def fizzbuzz(n):
    answer = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))