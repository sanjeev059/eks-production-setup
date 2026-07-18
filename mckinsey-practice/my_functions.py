# Function Exercises (Medium → Difficult)
# 🟢 Level 1 – Convert your previous solutions into functions
# find_max(numbers) → Return the maximum element.
from django.db.models.fields import return_None


# find_min(numbers) → Return the minimum element.
# def find_min(min_ele_arry):
#     min_ele = min_ele_arry[0]
#
#     for i in range(len(min_ele_arry)):
#         if min_ele_arry[i] < min_ele:
#             min_ele = min_ele_arry[i]
#     return min_ele


# # find_second_largest(numbers)
# #min_arry = [159,5,9,7,98,4,]
# def find_second_largest(numbers):
#     if len(numbers) < 2:
#         return None
#     largest = numbers[0]
#     for i in range(1, len(numbers)):
#         if numbers[i] > largest:
#             largest = numbers[i]
#
#     second_largest = None
#
#     for i in range(len(numbers)):
#         if numbers[i] != largest:
#             second_largest = numbers[i]
#             break
#
#     if second_largest is None:
#         return None
#
#     for j in range(len(numbers)):
#         if numbers[j] > second_largest and numbers[j] != largest:
#             second_largest = numbers[j]
#     return second_largest
#
#
#
# # count_vowels(text)
# def count_vowels(text):
#     text = text.lower()
#     vowels_string = "aeiou"
#     count = 0
#     for i in range(len(text)):
#         if text[i] in vowels_string:
#             count = count + 1
#     return count
# # reverse_string(text)
# def reverse_string(text):
#     rev_str = ""
#     for i in range(len(text) -1, -1,-1):
#         rev_str = rev_str + text[i]
#     return rev_str
#
# # is_palindrome(text) → Return True/False.
# def is_palindrome(text):
#     rev_str = ""
#     for i in range(len(text) - 1, -1, -1):
#         rev_str = rev_str + text[i]
#
#     if rev_str == text:
#         return True
#     else:
#         return False
# # remove_duplicates(text)
# def remove_duplicates(text):
#     dup_string = ""
#
#     for i in range(len(text)):
#         if text[i] in dup_string:
#             pass
#         else:
#             dup_string = dup_string +  text[i]
#     return dup_string
#
#
# # character_frequency(text) → Return a dictionary.
# def character_frequency(text):
#     char_freq = {}
#
#     for i in range(len(text)):
#         if text[i] in char_freq:
#             char_freq[text[i]] = char_freq[text[i]] + 1
#         else:
#             char_freq[text[i]] = 1
#     return  char_freq
#
#
#
# # find_largest_word(sentence)
# def find_largest_word(sentence):
#     sentence = sentence.split()
#     larg = sentence[0]
#     for i in range(len(sentence)):
#         if len(sentence[i]) > len(larg):
#             larg = sentence[i]
#
#     return larg
#
#
# # count_upper_lower(text) → Return both counts.
#
# def count_upper_lower(text):
#     count_upper = 0
#     count_lower = 0
#
#     for i in range(len(text)):
#         if text[i].isupper():
#             count_upper += 1
#         elif text[i].islower():
#             count_lower += 1
#
#     return count_upper, count_lower
# # 🟡 Level 2 – Lists
# # remove_duplicates_from_list(numbers)
# def remove_duplicates_from_list(numbers):
#     dup_list = []
#
#     for n in numbers:
#         if n in dup_list:
#             pass
#         else:
#             dup_list.append(n)
#     return dup_list
# count_even(numbers) # count_odd(numbers)
# def count_even(numbers):
#     count_even = 0
#     count_odd = 0
#
#     for n in numbers:
#         if n % 2 == 0:
#             count_even += 1
#         else:
#             count_odd += 1
#     return count_even, count_odd
# # sum_of_list(numbers)
# def sum_of_list(numbers):
#     total = 0
#     for n in numbers:
#         total = total + n
#     return total
# # average(numbers)
# def average(numbers):
#just take total divide it by lenght of list that give avergafe

# move_zeros(numbers)
# def move_zeros(numbers):
#     res = []
#     total_zero = 0
#     for n in numbers:
#         if n != 0:
#             res.append(n)
#         else:
#             total_zero = total_zero +1
#
#     for i in range(total_zero):
#             res.append(0)
#     return res
# # find_duplicates(numbers)
#
# def find_duplicates(numbers):
#     duplicate = []
#     seen = []
#
#     for nu in numbers:
#         if nu in seen and nu not in duplicate:
#             duplicate.append(nu)
#         else:
#             seen.append(nu)
#
#     return  duplicate


# merge_lists(list1, list2) --> did already

# # rotate_left(numbers, k)
# def rotate_left(numbers, k):
#
#     for i in range(k):
#         last = numbers.pop(0)
#         numbers.append(last)
#
#
# # rotate_right(numbers, k)
#
# def rotate_right(numbers, k):
#
#     for i in range(k):
#         first = numbers.pop(-1)
#         numbers.insert(0, first)
# # 🟡 Level 3 – Dictionary
# # word_frequency(sentence)
# def word_frequency(sentence):
#     sentence = sentence.split()
#
#     word_freq = {}
#
#     for word in sentence:
#         if word in word_freq:
#             word_freq[word] = word_freq[word] + 1
#         else:
#             word_freq[word] = 1
#     return  word_freq


# number_frequency(numbers) ---> same as above
# find_max_value_key(dictionary)

# def find_max_value_key(dictionary):
#     max_key = 0
#     max_value = 0
#     for k,val in dictionary.items():
#         max_key = k
#         max_value = val
#         break
#
#     for key,value in dictionary.items():
#         if value > max_value:
#             max_key = key
#             max_value = value
#     return max_key



# find_min_value_key(dictionary) --> change it to smaller
# reverse_dictionary(dictionary)

# def reverse_dictionary(dictionary):
#     new_dict = {}
#
#     for key,value in dictionary.items():
#         new_dict[value] = key
#     return new_dict
# merge_dictionary(dict1, dict2)
# def merge_dictionary(dict1, dict2):
#     new_dict = {}
#     for k,v in dict1.items():
#         new_dict[k] = v
#     for k,v in dict2.items():
#         new_dict[k] = v
#     return  new_dict
# key_exists(dictionary, key) --> skipped
# value_exists(dictionary, value) --> skipped
# 🟠 Level 4 – Interview Problems
# is_anagram(str1, str2)
# first_non_repeating(text)
# first_repeating(text)
# two_sum(numbers, target)
# missing_number(numbers)
# second_largest(numbers)
# binary_search(numbers, target)
# linear_search(numbers, target)
# valid_parentheses(text)
# longest_common_prefix(words)
# 🔴 Level 5 – Recursive Functions
# factorial(n)
# fibonacci(n)
# sum_of_digits(n)
# power(x, y)
# reverse_string_recursive(text)
# 🔵 Level 6 – File Handling
# read_json(filename)
# read_csv(filename)
# count_lines(filename)
# count_words(filename)
# count_characters(filename)
# 🟣 Level 7 – DevOps (Very Relevant for You)
# count_errors(logfile)
# count_warnings(logfile)
# extract_ips(logfile)
# extract_timestamps(logfile)
# find_most_common_error(logfile)
# # parse_cloudwatch_logs

if __name__ == "__main__":
    min_arry = [159,5,9,7,98,4]
    # min_ele = find_min(min_arry)
    # print(min_ele)
    # second_large = find_second_largest(min_arry)
    # print(second_large)
    text = "sanjeev"
    # count  = count_vowels(text)
    # print(count)
    # text_repet = "sanjeevdesai"

    # char_freq = character_frequency(text_repet)
    # print(char_freq)

    # sentence = "i love programing"
    # large = find_largest_word(sentence)
    # print(large)
    dict1 = {'a':1,'b':2}
    dict2 = {'c':3,'d':4}
    new_dict = merge_dictionary(dict1, dict2)
    print(new_dict)