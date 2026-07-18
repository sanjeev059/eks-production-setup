# Add elements to a set.
def add_ele_to():
    seen  = set()
    seen.add("a")
    print(seen)
    seen.discard("a")
    print(seen)
# Remove elements.
# Check membership using in.
def check_member():
        fruits = {"apple", "banana", "orange", "mango"}
        if "banana" in fruits:
            return True
        else:
            return False
# Remove duplicates from a list.
def remove_duplicates():
    cities = [
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Bangalore",
        "Pune",
        "Chennai"
    ]
    dup_list = list(set(cities))
    print(dup_list)

# Remove duplicates from a string.
def remove_duplicates_from_a_string():
    str_sub = "programming"
    res = []
    seen = set()
    for ch in str_sub:
        if ch in seen:
            pass
        else:
            seen.add(ch)
            res.append(ch)
    print(res)


# Find common elements between two sets.
def common_elements():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    res = set()
    for n in set2 and set1:
        if n in set1 and n in set2:
            res.add(n)
    print(res)
    # res = set1.intersection(set2)
    # print(res)

# Find unique elements in the first set.
def unique_elements():
    set1 = {1, 2, 3, 4, 5}
    set2 = {3, 4, 5, 6, 7}
    res = set()

    for unique_n in set1:
        if unique_n in set1 and unique_n not in set2:
            res.add(unique_n)
    print(res)
# Count distinct characters in a string.\
def count_distinct_characters():
    str_sub = "banana"
    seen = set()

    for ch in str_sub:
        if ch not in seen:
            seen.add(ch)
    print(len(seen))

# Check if two lists have any common element.
# Print only unique words from a sentence
def longest_substring_without_repeating_characters():
    str_sub = "abcacbdsf"
    seen = set()
    l = 0
    r = 0
    max_length  = 0
    while r < len(str_sub):
        if str_sub[r] not in seen:
            seen.add(str_sub[r])
            current_length = r - l + 1
            if current_length > max_length:
                max_length = current_length
            r = r + 1
        else:
            seen.remove(str_sub[l])
            l += 1
            current_length = r - l + 1
    print(max_length)


if __name__ == '__main__':
    # add_ele_to()
    # check = check_member()
    # print(check)
    # remove_duplicates()
    # remove_duplicates_from_a_string()
    # common_elements()
    unique_elements()
    count_distinct_characters()
    longest_substring_without_repeating_characters()