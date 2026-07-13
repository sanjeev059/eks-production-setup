# linear_search(numbers, target)
def linear_search(numbers, target):
    if target == numbers[0]:
        return 0
    if target == numbers[-1]:
        return len(numbers) - 1

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return "Not found"

# binary_search(numbers, target)
# binary_search(numbers, target)
def binary_search(numbers, target):
    first = 0
    last = len(numbers) - 1

    while first <= last:
        mid = (first + last) // 2

        if target == numbers[mid]:
            return mid

        elif numbers[mid] > target:
            last = mid - 1

        else:
            first = mid + 1

    return -1



# find_second_largest(numbers)
def find_second_largest(numbers):
    first_lar = numbers[0]

    for i in range(len(numbers)):
        if numbers[i] > first_lar:
            first_lar = numbers[i]

    second_lar = None

    for i in range(len(numbers)):
        second_lar = numbers[i]
        break

    for j in range(len(numbers)) :
        if numbers[j] > second_lar and numbers[j] != first_lar:
            second_lar = numbers[j]
    return second_lar


# find_second_smallest(numbers)
# missing_number(numbers)
def missing_number(numbers):
    exp = 1

    for i in range(len(numbers)):
        if numbers[i] == exp:
            exp += 1
    return exp


# move_zeros(numbers)
def move_zeros(numbers):
    res = []
    count = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            res.append(numbers[i])
        else:
            count += 1
    for i in range(count):
             res.append(0)
    return res





# find_duplicates(numbers)
def find_duplicates(numbers):
    seen = []
    duplicates = []

    for i in range(len(numbers)):
        if numbers[i] in seen:
            duplicates.append(numbers[i])
        else:
            seen.append(numbers[i])
    return seen

# remove_duplicates(numbers)
# reverse_list(numbers)
# rotate_left(numbers, k)
# rotate_right(numbers, k)

if __name__ == '__main__':
    numbers = [40,10,44,3,6,7]
    target = 44
    pos =  linear_search(numbers, target)
   
    print(pos)
    numbers_b = [40, 10, 44, 3, 6, 7]
    target = 3
    bin_pos = binary_search(numbers_b, target)
    print(bin_pos)
    mov_zeros = [1,2,0,1,0,3,0,2]
    res_list = move_zeros(mov_zeros)
    print(res_list)

    numbers = [2,2,3,4,5,4,3,2,6,7,7]
    nums = find_duplicates(numbers)
    print(nums)