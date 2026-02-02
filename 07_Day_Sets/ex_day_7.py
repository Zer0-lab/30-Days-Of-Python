# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))  # 7

it_companies.add('Twitter')
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}

it_companies.update(['LinkedIn', 'Snapchat', 'Pinterest'])
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', ['LinkedIn', 'Snapchat', 'Pinterest']}

it_companies.remove('IBM')
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon', 'Twitter', ['LinkedIn', 'Snapchat', 'Pinterest']

# Remove an item from a set using remove() method. If the item is not found remove()
# method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

it_companies.discard('IBM')
print(it_companies)  # {'Facebook', 'Google', 'Microsoft', 'Apple', 'Oracle', 'Amazon', 'Twitter', ['LinkedIn', 'Snapchat', 'Pinterest']}

A_union_B = A.union(B)
print(A_union_B)  # {19, 20, 22, 24, 25, 26, 27, 28}

A_intersection_B = A.intersection(B)
print(A_intersection_B)  # {19, 20, 22, 24, 25, 26}

A_subset_B = A.issubset(B)
print(A_subset_B)  # False

A_disjoint_B = A.isdisjoint(B)
print(A_disjoint_B)  # False

A_sym_diff_B = A.symmetric_difference(B)
print(A_sym_diff_B)  # {27, 28}

del it_companies

age_set = set(age)
print(age_set)  # {19, 22, 24, 25, 26}

print(len(age) == len(age_set))  # False

# The difference between string, list, tuple and set is that
# string, list and tuple are ordered collections of items whereas set is an unordered collection of unique items.
# Also, string is a collection of characters, list and tuple can contain any data type,
# but set only contains unique items and does not allow duplicates.
# Lists are mutable, meaning we can change, add, or remove items after its creation.
# Tuples are immutable, meaning once they are created, their items cannot be changed, added, or removed.
# Sets are mutable, meaning we can add or remove items after its creation.
# However, the items in a set must be immutable (e.g., strings, numbers, tuples).
# Sets do not support indexing, slicing, or other sequence-like behavior
# because they are unordered collections.
# Sets are optimized for membership testing and eliminating duplicate entries from a collection.
# Sets support mathematical operations like union, intersection, difference, and symmetric difference.
# Sets are commonly used when the existence of an item in a collection is more important than the order or how many times it occurs.

