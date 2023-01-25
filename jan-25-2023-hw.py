from itertools import zip_longest

"""
 Find all occurrences of a substring in a given string by ignoring the case
"""
str1 = "Welcome to USA. usa awesome, isn't it?"
# -> The USA count is: 2
#HINT: use split() to get started

substring = "usa"
count = str1.lower().split().count(substring.lower())
print("The USA count is:", count)

"""
Create a mixed String using the following rules
Given two strings, s1 and s2.
Write a program to create a new string s3 made of the first char of s1, 
then the last char of s2,
Next, the second char of s1 and second last char of s2, and so on. 
Any leftover chars go at the end of the result.

"""
s1 = "Abc" #read s1 from left to right
s2 = "Xyz"[::-1] # read s2 from right to left
# -> AzbycX

s3 = "".join(char1 + char2 for char1, char2 in zip_longest(s1, s2, fillvalue=""))
print(s3)