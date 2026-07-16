# ✅ Find First Mismatch
# ✅ Return All Valid Removal Indices
# ✅ Merge Two Sorted Arrays
# ✅ Remove Duplicates from Sorted Array
# ✅ Move All Zeros
# ✅ Valid Palindrome
# ✅ Two Sum
# ✅ Longest Substring Without Repeating Characters
# ✅ Container With Most Water
# ✅ Trapping Rain Water
# from operator import truediv


def longest_substring_without_repeating_characters():
    seen = set()
    str_sub = "abca"
    for ch in str_sub:
        if ch in seen:
            print(ch, "is duplicate")
        else:
            seen.add(ch)

# a = [1,2,3,4,5]
# target = 8
def two_sum(a, target):

    l = 0
    r = len(a) -1

    while l < r:
        if a[l] + a[r] != target and a[l] + a[r] < target:
            l = l +1
            return [l,r]
        else:
            r = r - 1
            return [l, r]





def valid_palindrome(s):
    l = 0
    r = len(s) -1

    while l < r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True

# s1 = "sanjeeev"
# s2 = "sanjeev"
def all_valid_removal_indices(str1, str2):
    new_str = ""
    result = []
    for i in range(len(str1)):
        new_str = str1[:i] + str1[i+1:]

        if new_str == str2:
            result.append(i)
    print(result)

# arr1 = [1, 3, 5, 7]
# arr2 = [2, 4, 6, 8]

def merge_two_sorted_arrays(a1, a2):
    res_array = []
    p1 = 0
    p2 = 0
    while p1 < len(a1) and p2 < len(a2):
        if a1[p1] < a2[p2]:

            res_array.append(a1[p1])
            p1 += 1
        else:
            res_array.append(a2[p2])
            p2 += 1
    while p1 < len(a1):
        res_array.append(a1[p1])
        p1 += 1

    # Add remaining elements from a2
    while p2 < len(a2):
        res_array.append(a2[p2])
        p2 += 1

    print(res_array)

def remove_duplicates_from_sorted_array(a):
    i = 0
    j = 1

    while j < len(a):
        if a[i] != a[j]:
            a[i+1] = a[j]
            i += 1
            j += 1
        else:
            j += 1
    print(a)

def  move_all_zeros(a):
    i = 0
    j = 0

    while j < len(a):
        if a[j] != 0:
            a[i] = a[j]
            i += 1
            j += 1
        else:
            j += 1
    while i < len(a):
        a[i] = 0
        i += 1
    print(a)

if __name__ == '__main__':

    # s1 = "sanjeeev"
    # s2 = "sanjeev"
    # all_valid_removal_indices(s1, s2)
    #
    # arr1 = [1, 3, 5, 7]
    # arr2 = [2, 4, 6, 8]
    # merge_two_sorted_arrays(arr1, arr2)
    #
    # numbers = [1, 1, 2, 2, 3, 3, 4]
    # remove_duplicates_from_sorted_array(numbers)
    # numbers = [0,1,0,3,12]
    # move_all_zeros(numbers)
    #
    # a = [1,2,3,4,5]
    # target = 8
    # omd = two_sum(a, target)
    # print(omd)

    longest_substring_without_repeating_characters()