## Exercise 2
You've been given data for the number of new COVID-19 cases per day for the month of March.
```python
daily_new_cases = {
    'March 1':1981,
    'March 6':3625,
    'March 16':12920,
    'March 26':60994,
    'March 31':73792
    }
```
The data was measured in five-day intervals, though two values are missing: March 11th and March 21st. Here's what you need to do:

- Create a scatterplot of the data given to you, and include axis labels and a title. The color of each point should be orange.
- Find an equation for the line of best fit.
- Using your equation, approximate the values for the missing datapoints.

**Hint**: While plotting, remember that two of the values are missing.

## Exercise 3

You've just finished an experiment to calculate a spring constant. Here is the data in a list:
```python
# data is in the form [mass, T^2, uncertainty of T^2]
data = [
[0.051,0.09,0.006]
[0.102,0.16,0.003]
[0.153,0.23,0.003]
[0.204,0.30,0.003]
[0.255,0.38,0.001]
[0.306,0.45,0.003]
[0.357,0.52,0.004]
[0.408,0.59,0.006]
[0.459,0.66,0.010]
[0.510,0.73,0.020]
]
```
What you need to do:
- Reorganize the data to make it easier for you to plot.
- Plot three different lines:
	- The line of the graph T^2 against mass, with error bars.
	- The line of maximum gradient
	- The line of minimum gradient
- Label each axis and give the plot a title. Make sure each line is colored differently. Include a legend in the plot.
