"""
Variables and Data Types
"""

"""
int - An integer
"""
# 'L' is the string length
L = 20

"""
float - A 'floating point' value: any number that has a decimal point in it
"""
# 'T' is the time taken for 15 oscillations
T = 13.65

"""
str - A sequence or 'string' of characters - always use double/single quotes around a string
"""
ball_material = "steel"

"""
list - A collection of related values. Place values in square brackets and separate with commas.
"""
# A list of 'int' values. Stores the lengths of the string used in the experiment
lengths = [15, 20, 25, 30, 35, 40, 45, 50, 55, 60]

# A list of 'float' values. Stores the times taken for 15 oscillations
T_list = [11.70, 13.60, 15.10, 16.60, 17.75, 19.05, 19.50, 21.05, 22.50, 23.75]

# Note: a list can contain lists inside it as shown below
sample_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

"""
dictionary - a list of mappings of one value to another.
"""
# a mapping of L to T. Inside curly brackets, mapped with colons, separated with commas.
T_dict = {15:11.70, 20:13.60, 25:15.10, 30:16.60, 35:17.75,
            40:19.05, 45:19.50, 50:21.05, 55:22.50, 60:23.75}

"""
Boolean - takes one value, either True, or False
"""
x = True
x = False
# the value True is stored in the variable within_bounds, since the statement '9 < g < 11' is true.
g = 10.1

within_bounds = 9 < g < 11 #True
# the value True is stored in the variable within_bounds, since the statement '9 < g < 11' is true.

# In contrast, if the statement '9 < g < 11' is not true, the value False will be stored in the variable within_bounds

g = 12

within_bounds = 9 < g < 11 #False
