from pprint import pprint as pp

"""
Total counts of chars, digits, and symbols 

Chars = 8 
Digits = 3 
Symbol = 4

"""
str1 = "P@#yn26at^&i5ve"
# define an empty dictionary
count_dict = {
    'digit_count':0,
    'char_count':0,
    'symbol_count':0,
    'digit_count1':1,
    'char_count1':1,
    'symbol_count1':1
}

for char in str1:
    if char.isdigit():
        count_dict['digit_count'] += 1 # digit_count  = digit_count + 1
    elif char.isalpha():
        count_dict['char_count'] += 1
    else:
        count_dict['symbol_count'] += 1

# printing out dictionaries requires a bit of a special function items()
for k,v in count_dict.items():
    print(f"key: {k}, value: {v}")

# regular iteration will just iterate over the keys
for entry in count_dict:
    print(entry)


# print(count_dict)
# #print(f"digit count {count_dict['digit_count']}")
# pp(count_dict)