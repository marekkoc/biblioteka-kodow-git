from collections import deque


# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original set:", my_set)

# Trying to add a duplicate element
my_set.add(3)  # No effect, as 3 is already in the set
print("After attempting to add a duplicate:", my_set)


# Convert list to set
my_list = [1, 2, 3, 4, 5, 3, 2, 1]
my_set = set(my_list)
my_list = list(my_set)
print("Set from list:", my_set)
print("list with only unique values", my_list)


# Sets do not allow duplicate elements

# Creating a frozen set
my_frozen_set = frozenset([1, 2, 3, 4, 5])
print("Frozen set:", my_frozen_set)

# Frozen sets are immutable
# my_frozen_set.add(6)  # This will raise an AttributeError


# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])
print("Original deque:", my_deque)

# Adding elements at both ends
my_deque.append(6)  # Add at the end
my_deque.appendleft(0)  # Add at the start
print("After adding elements:", my_deque)

# Removing elements from both ends
my_deque.pop()  # Remove from the end
my_deque.popleft()  # Remove from the start
print("After removing elements:", my_deque)
