from week1_datatypes import *

"""
Operators
"""

"""
Mathematical
"""
uncertainty = 0.001
# Addition
y_max = T + uncertainty
# Subtraction
y_min = T - uncertainty

# Multiplication
product = T * 2

# Division: always returns a float
# Changing units to meters for length measurement
L_in_meters = L / 100

# where 't' is the time taken for one oscillation
t = T/15

# Exponents
t_squared = t ** 2

# Modulo - returns the remainder when dividing integers a and b - a % b
a = 10
b = 3
rem = 10 % 3
"""
Manipulating lists
"""
# Accessing an element of a list
# Remember: lists always start with an index of 0. This means that the first element of the list has an index 0
T_list = [11.70, 13.60, 15.10, 16.60, 17.75, 19.05, 19.50, 21.05, 22.50, 23.75]
t = T_list[0] # Returns the first element of the list, which is 11.70
t = T_list[4] # Returns the third element of the list, which is 16.60

# Adding an element to a list(or 'appending' an element, rather)

T_list.append(25.5) # Append adds the element in the brackets to the list.

# Removing an element from the list using the element value

T_list.remove(25.5) # Removes the first element that is found that matches the element in the brackets. If there is no such element, a ValueError occurs.

# Removing an element from a list using the position

T_list.pop([4]) # Removes the element in the 4th index(or third position) from the list.

# Remove the last element from the list

T_list.pop() # Removes the last element, which in this case is 23.75

# Removing all elements from a list

T_list.clear()

# Sort elements in a list in ascending order

T_list.sort() # sorts the numbers in the list in ascending order

# Sort elements in a list in descending order

T_list.reverse() # sorts the numbers in the list in descending order

"""
Manipulating dictionaries
"""
# Searching for a value using the key

T_dict = {15:11.70, 20:13.60, 25:15.10, 30:16.60, 35:17.75,
            40:19.05, 45:19.50, 50:21.05, 55:22.50, 60:23.75}

t = T_dict[15] # Outputs 11.70, since that is the value of this key-value pair. If the key does not exist, then a ValueError occurs

# Update an existing entry

T_dict[20] = 12.30 # Replaces the value 13.60 with 12.30

# Add a new entry

T_dict[65] = 25.5 # adds a new key-value pair which is 65: 25.5

# Delete an entry using the key

del T_dict[60] # Deletes the entry with 60:23.75

# Remove all entries in an entire dictionary

T_dict.clear()

# Delete an entire dictionary

del T_dict
