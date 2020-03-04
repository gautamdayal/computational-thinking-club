# Loops and lists 

## Example 1
- **Question:** Create a list containing 5 numbers. Find the average of these numbers and print it. 
- **Answer:**
	```python
	numbers = [90, 80.25, 340, 2, 123.456]
	total = 0
	for x in numbers:
		# remember, x points to an element, not its index
		total = total + x
	# note that the average is found OUTSIDE the loop
	average = total / 5
	print(average)
	```
- **Explanation:**
	Here, the for loop iterates over all the numbers in the loop and adds each to the variable `total` one by one. Hence, when the program exits the for loop, `total` contains the sum of all the numbers in the list. 
- **Output:**
	```
	127.1412
	```

## Example 2
- **Question:** Find the maximum number in a list of 10 elements and print it. 
- **Answer:**
	```python
	numbers = [15, 0, -340, 3.14, 151, 1, 90, 359.1, 4, 10]
	# Declaring a variable and essentially assigning it 
	# nothing as a value:
	maximum = numbers[0]
	for y in numbers:
		if y > maximum:
			maximum = y
	print(maximum)
	```
- **Output:**
```
359.1
```

## Example 3

- **Question:** Input a word from the user and reverse it. Print the reversed string. 
- **Answer:**
	```python
	user_word = input("Tell me a word")
	# len() is a built-in function that returns 
	# the number of elements contained within the list 
	word_length = len(user_word)
	# list() is a built-in function that converts a string 
	# into a list of characters and returns it
	word_list = list(user_word)
	print(word_list)
	reversed_word_list = []
	for i in range((word_length - 1), -1, -1):
		reversed_word_list.append(word_list[i])
	print(reversed_word_list)
	reversed_word = "".join(reversed_word_list)
	print(reversed_word)
	```
- **Explanation:** The loop looks a bit complicated, so here's an explanation for what it does:
	```python
	for i in range((word_length - 1), -1, -1)
	```
	The goal of this loop is to essentially iterate backwards from the end of the list to the start, and append each element to a new list. 

	The range function takes three arguments: range(start, stop, step). Remember, start <= i  __==<==__ stop. Since the highest index of the list that we want to start from would be (number of elements - 1), this is given as the start value. The lowest index we would want to stop at would be 0. Hence, the stop value is given as -1. Finally, as we want to decrement, the step value is -1. 
	
	Once we exit the loop, we now have a list containing all the letters of the word in reverse order so we use the .join() method to make the list a string. 
	
- **Output:** 
```
Tell me a word:hello
["h", "e", "l", "l", "o"]
["o", "l", "l", "e", "h"]
olleh
```

## Example 4
- **Question:** Input the length of three sides of a triangle and print whether the triangle is equilateral, isosceles or scalene
- **Answer:**
	```python
	sides = []
	i = 0
	while i < 3:
		sides.append(input("Length of side " + str(i) +  " of the triangle:"))
		i = i + 1
	if sides[0] == sides[1] == sides[2]:
		print("It is an equilateral triangle")
	elif sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]:
		print("It is an isoceles triangle")
	else:
		print("It is a scalene triangle")
	```
- **Output:**
	```
	Length of side 1 of the triangle: 15
	Length of side 1 of the triangle: 45
	Length of side 1 of the triangle: 45
	It is an isoceles triangle 
	```

## Problem 5

- **Question:** Write a program that takes a 4-digit number as input and prints the average of the digits. 
