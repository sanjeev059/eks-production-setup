# Easy (finish all of these)
# ✅ Palindrome
# Count vowels
# mystr = str(input())
# owels = ['a','e','i','o','u']
# count = 0
# for i in range(len(mystr)):
#     if mystr[i] in owels:
#         count = count + 1
#
# print(count)
# Count consonants
# mystr = str(input())
# owels = ['a','e','i','o','u']
# count = 0
# for i in range(len(mystr)):
#     if mystr[i] not in owels:
#         count = count + 1
# print(count)
# Reverse a string
from itertools import count
from operator import truediv

from django.template.defaultfilters import first

# rev_str = input()
# print(rev_str[: : -1])
# Reverse each word in a sentence

# sentece = input().split(" ")
# i = 0
# rev_str = []
# for word in sentece:
#     rev_str.append( word[::-1])
# rev_str = " ".join(rev_str)
# print(rev_str)



# Count uppercase/lowercase letters
# input_str = input()
# upper_cont = 0
# lower_count = 0
# for i in range(len(input_str)):
#     if input_str[i].isupper():
#         upper_cont = upper_cont + 1
#     elif input_str[i].islower():
#         lower_count = lower_count +1
# print("upper_count :", upper_cont)
# print("lower_count :", lower_count)

# Count spaces
# space_str = input()
# counter = 0
#
# for i in range(len(space_str)):
#     if space_str[i] == " ":
#         counter = counter + 1
# print(counter)

# Remove duplicate characters

# dup_str = input()
#
# cat_dup = ""
#
# for i in range(len(dup_str)):
#     if dup_str[i] in cat_dup:
#         pass;
#     else:
#         cat_dup = cat_dup + dup_str[i]

# print(cat_dup)

# # Find the largest word
# large_word = input().split()
#
# largest_world = ""
# for i in range(len(large_word)):
#     if len(large_word[i]) > len(largest_world):
#         largest_world = large_word[i]
# print(largest_world)

# Count character frequency
# my_input_string = "Sanjeev"
#
# freq = {}
#
# for ch in my_input_string:
#
#     if ch in freq:
#         freq[ch] = freq[ch] + 1
#     else:
#         freq[ch] = 1
#
# print(freq)

# #Arrays in details
#
# # Print first element
#
# n = [20,3,4,78,90,100]
#
# # Print last element
# print(n[0])
# # Find length
# print(len(n))
# # Append
# n.append(200)
# print(n)
# # Remove
# n.remove(78)
# print()
# # Insert
# n.insert(3,30)
# print(n)
# # Reverse
# for i in range(len(n)-1):
#     print(n[-i])
# # Find max
# maximum = 0
# for i in range(len(n)-1):
#     if n[i] > maximum:
#         maximum = n[i]
# print("maximum number = ",maximum)
# # Find min
# mini = 0
# for i in range(len(n)-1):
#     if n[i] < mini:
#         mini = n[i]
# print("minimum:", min)
#
# # Traverse
# for i in range(len(n)):
#     print(n[i])
#

# Create a dictionary.
my_dict = {
    20: "a",
    40: "b",
    60: "c",
    80: "d",
    100: "e"
}
# Access values using keys.
for key, value in my_dict.items():
    if key == 100:
        print(value)


# Add a new key-value pair.
my_dict[120] = "k"
print(my_dict)
# Update an existing value.
for key,value in my_dict.items():
    if key == 40:
        my_dict[key] = "man"
print(my_dict)
# Delete a key
del my_dict[20]
print(my_dict)

# Challenge for you: How would you delete all keys whose value is "a"?
for key,value in my_dict.items():
    if my_dict[key] == "a":
        del my_dict[key]
print("delete key whose value is a",my_dict)

# Print all keys.
for key in my_dict:
    print(key)
# Print all values.
for key in my_dict:
    print(my_dict[key])
# Iterate using items().
for key,value in my_dict.items():
    print(key,value)
# Check if a key exists.
check = False
for key,value in my_dict.items():
    if key == 500:
        check = True
print(check)

# Count the frequency of numbers in a dict.
count = 0
target_number = 30
for key,value in my_dict.items():
    if key == target_number:
        count += 1
print(count)
# Find the key with the maximum value.
max_val = 0
marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95
}
for key, value in marks.items():
    if marks[key] > max_val:
        max_val = marks[key]
print(max_val)



# Medium --> Pending items to finish
# Two Sum
# Find Missing Number
# Remove Duplicates from List
# Anagram
# First Non-Repeating Character
# Fibonacci (iterative & recursive)
# Prime Number
# Valid Parentheses
# Frequency Counter
# Read JSON
# Read CSV
# Log Parsing (ERROR/WARNING/INFO)
# Find Duplicate Elements
# Second Largest Number
# Merge Two Lists
