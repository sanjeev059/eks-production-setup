# Next: Sets
#
# Practice these basics:
#
# Create a set.
num = {3,4,2,5,6,7,8,9}
# Add an element.
num.add(10)
print(num)
# Remove an element.
num.remove(5)
print(num)
# Check if an element exists.
target = 40
check = False
for i in num:
    if i == target:
        check = True
print(check)
# Iterate through a set.

for n in num:
    print(n)

# Remove duplicates from a list using a set.
dup_array = [1,3,2,3,2,4,5,6]
set_list = set(dup_array)
print(set_list)
# Union of two sets.
set_first = {1,3,4,5,6,7,8}
set_two = {6,3,5,6,2,1,5}

unique_set = set_first.union(set_two)
print("union of two sets",unique_set)
# Intersection of two sets.

inter_set = set_first.intersection(set_two)
print("intersecton of two sets",inter_set)
# Difference of two sets.

# Symmetric difference.
# Convert a list to a set.
# Count unique elements.