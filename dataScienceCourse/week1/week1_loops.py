"""
Loops
"""

"""
The for Loop - iterates (travels one by one) through a set of values

for [variable] in [set of values]:
    [do something]
"""
# Make sure that [do something] is indented - use the tab key for this
# [variable] does not need to be defined before the loop

# list of length measurements in centimeters
L = [0, 10, 20, 30, 40, 50, 60, 70]
L_meters = []

# A simple for loop that converts each measurement to meters
for length in L: # This for loop takes one element from the list L at a time and stores that in the element length. It does this for all elements in the list.
    L_meters.append(length/100) # Converts the length to metres using 'length/100'. Adds the metre converted length to a new list called L_meters

"""
In the above case:
[variable] = length
[set of values] = L
[do something] = L_meters.append(length/100)
"""

# We can also iterate over a range ([do something] a certain number of times)

"""
Range takes in 3 parameters, the starting value, the ending value, and the increment or decrement

range([starting_parameter], [ending_parameter], [increment])
"""

# A simple for loop using range
for i in range(1, 6, 1): # if we say this, this means after each time the code runs, the value of i increments by 1[since increment = 1] from 1 till 6
    [code]

# Note that i never takes the ending_parameter's value, so it will never reach 6. i will take 1, 2, 3, 4, 5.

# A double increment for loop

for i in range(1, 10, 2): # The increment is 2, so the values that i takes are 1, 3, 5, 7, 9
    [code]
# Decrement for loop

for i in range(10, 1, -1): # counts down from 10 till 1, as the increments are -1 or a decrement of 1. The values that i takes are 10, 9, 8, 7, 6, 5, 4, 3, 2.
    [code]

# Default values for Range

for i in range(6): # if only one parameter is passed, it is assumed to be the final value or ending parameter. The default starting value is 0 and the default increment is 1 as well.
    [code]

for i in range(1, 7) # if two parameters are given, the first is assumed to be the starting value and the last is assumed to be the ending value. The default increment is taken to be 1.



# List of time periods for 15 oscillations for a certain length
T = [11.70, 12.00, 11.55]
total = 0
# for loop that sums each value in T - this sum can later be used to find the mean value

for i in range(len(T)): # len(T) returns the length of the list, in this case it is 3 as there are 3 elements in T
    total += T[i]

# The range is the range of values that i can take, which is from 0 till 3 (since 3 is the length)

"""
Try it yourself
[variable] =
[set of values] =
[do something] =
"""

"""
The while Loop

while [boolean expression is True]:
    [do something]
    [update variable in boolean expression]

Note: a while loop stops only if the boolean eventually becomes False. Beware of forever loops in your code.
"""

# Forever loop

while 2 > 1: # since the expression 2 > 1 is always true, the loop continues to run endlessly, forever.
    [code]

# The meter conversion, but this time using a while loop
i = 0
L_m = []
while i < len(L): # While the expression i < len(L) is true the loop runs. len(L) refers the length of the list, which is 3 in this case as it contains 3 elements.
    L_m.append(L[i]/100)
    i += 1

"""
In the above case:

[boolean expression] = i < len(L)
[do something] = L_m.append(L[i]/100)
[update variable in boolean expression] = i += 1
"""
