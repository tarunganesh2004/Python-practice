# to create a set with items 
items={"apple","banana","cherry","apple","banana"}
print(items)  # Output: {'banana', 'cherry', 'apple'}

# to create an empty set
empty_set=set()
print(empty_set)  # Output: set()

# to add an item to a set
items.add("orange")
print(items)  # Output: {'banana', 'cherry', 'apple', 'orange'}

#set functions
"""
add - adds an element to the set s.add(e)
remove - removes an element from the set s.remove(e)
discard - removes an element from the set if it is a member. If not a member, do nothing s.discard(e)
pop - removes and returns an arbitrary element from the set s.pop()
clear - removes all elements from the set s.clear()

union - returns a new set with elements from both sets s1.union(s2)
intersection - returns a new set with elements common to both sets s1.intersection(s2)
difference - returns a new set with elements in the first set but not in the second s1.difference(s2)
symmetric_difference - returns a new set with elements in either the first or the second set but not in both s1.symmetric_difference(s2)
"""