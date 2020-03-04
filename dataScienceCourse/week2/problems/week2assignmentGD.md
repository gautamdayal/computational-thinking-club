# Lists, Loops, and Conditionals.
We've included 4 example problems, which we encourage you to play around with on your own computers. Finally, there is  a problem which you'll have to submit. Have fun!
## Example 1
- **Question:** Get the user to input 5 different integers to a list. Then, print out whether each number is even or not, in the format *Yes, [number] is even*, or *No, [number is odd]*.
- **Solution:**
```python
L = []
for i in range(5):
	x = int(input("Enter number: "))
	L.append(x)
	
for n in L:
	if n % 2 == 0:
		print("Yes, " + str(n) + " is even")
	else:
		print("No, " + str(n) + " is odd")
```
- **Explanation:**
	- We create a list 'L'
	- Get the user to input an integer 'x' five times, and add x to L each time
	- Go through each element of L, check if the remainder when dividing by 2 is zero; if yes, the number is even
	
- **Output:**
```
Enter number: 5
Enter number: 7
Enter number: 8
Enter number: 9
Enter number: 4
No, 5 is odd
No, 7 is odd
Yes, 8 is even
No, 9 is odd
Yes, 4 is even
```

## Example 2
- **Question:** Given a string input by the user, add each vowel in the string to a list, and print this list out. Also print out the number of vowels in the input text. Note that the text could be either upper or lower case. 
- **Solution**
```python
text = input("Enter some text: ")
vowels = "aeiouAEIOU"
vowel_list = []
for c in text:
	if c in vowels:
		vowel_list.append(c)

print(vowel_list)
print(len(vowel_list))
```
- **Output**
```
Enter some text: Lorem Ipsum Dolor Sit Amet
['o', 'e', 'I', 'u', 'o', 'o', 'i', 'A', 'e']
9
```
- **Explanation**
	-	Input a string and store it in a variable called text
	-	Create a string with each vowel, **both uppercase and lowercase**. This is because Python looks at 'A' and 'a' to be different values. 
	-	Go through each element in text, check whether it's in vowels. If it is, add this to vowel_list
	-	After the loop, print out vowel_list and its length. 

## Example 3
- **Question:** Given a list of integers, print out the first three values in the list that are greater than ten. Even though there are more than three, only print out the first three. **Use a while loop in your program**. Use the following list: [12, 29, 5, 3, 34, 7, 50, 45]

- **Solution**
```python
L = [12, 29, 5, 3, 34, 7, 50, 45]
i = 0
greater_than_ten = 0
while (greater_than ten != 3):
	if L[i] > 10:
		greater_than_ten = greater_than_ten + 1
		print(L[i])
	i = i + 1
```
- **Output**
```
12
29
34
```
- **Explanation**
	- Create a variable i to get each item in the list by indexing. 
	- Create a variable to store the number of values greater than ten we have already found.
	- While, the number of these values is not equal to 3
		- If the i'th element of L is greater than 10, print it out and increment greater_than_ten by 1
	- Increment i by 1
	
## Example 4
- **Question:** You are given a list of temperature measurements, but the units are celsius for some and fahrenheit for others. If a measurement is greater than 50, it is considered as fahrenheit. Convert all fahrenheit measurements to celsius, store them in a list, and print the list out. 

**Formula**: (F - 32) / 1.8 = C
**List of measurements**: [24, 67, 90, 12, 13, 20, 88, 76]
- **Solution**
```python
L = [24, 67, 90, 12, 13, 20, 88, 76]
to_celsius = []
for m in L:
	if m > 50:
		to_celsius.append((m - 32)/1.8)

print(to_celcius)
```
- **Output**
```
[19.444444444444443, 32.22222222222222, 31.11111111111111, 24.444444444444443]
```
- **Explanation**
	- Create a list to store any converted values 
	- Go through each measurement,
		- if it's greater than 50, 
			- add the converted value to to_celsius
	- print out to_celcius

## Problem
Now it's time to try a problem out for yourself. 
- **Question:** Print out a right aligned pyramid compose of the either the 'e' character or the 'o' character. Ask the user to input a desired number of rows. If the row number is even, the row must be made of the character 'e'. Otherwise, it should be made up of the character 'o'.
- **Output**
```
Enter number of rows: 5
    o
   ee
  ooo
 eeee
ooooo

```
Hint: you can multiply ints with strings. 

Good luck!