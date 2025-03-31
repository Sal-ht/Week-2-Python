# Create an empty list
my_list = []

# Append elements
my_list = [10, 20, 30, 40]

# Insert 15 into the second position (Index 1)
my_list.insert(1, 15)

# Extend list with another list 
my_list.extend([50,60,70])

# Remove last element
my_list.pop()

# Sort in asc order
my_list.sort()

# Index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Print final list
print(my_list)