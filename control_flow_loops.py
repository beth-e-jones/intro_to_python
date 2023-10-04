#%%
import pandas as pd

# %%
# Read in data
titanic = pd.read_excel("data/titanic.xlsx")
titanic.head()


# %%
animals = pd.read_csv("data/animals.csv")
animals.head() # Checks first five rows

# %%
""" 
Operator	Description
==	        Equivalent to
!=	        Not equivalent to
<	        Less than
<=	        Less than or equal to
>	        Greater than
>=	        Greater than or equal to
"""

# %%
# Some simple checks
print (4 ==2)

# %%
print (True > False)

# %%
# We can also apply this to pandas and check a variable against a value

# %%
(titanic["sex"] == "female").head()
# %%
""" Logical operators are used to join conditional statements, if we want to 
use more than one
 
Operator	Description
&	        And
|	        Or
!	        Not   
    
"""

# %%
"""" You can understand the outcomes of different conditions with a Truth Table

Condition 1	   Condition 2	    & (AND) Equates to	        | (OR) Equates to
True	        True	            True	                True
True	        False	            False	                True
False	        True	            False	                True
False	        False	            False	                False

"""

# %%
# You can filter dataframes using these conditional statements 

titanic_female_children = titanic[
    (titanic["sex"] == "female") & (titanic["age"]<18)
    ]
titanic_female_children.head()

# %%
"""
We can use conditional statements and comparisons when we make loops
(I looked up control flow, and it's the order python follows instructions)

2 types of loops - for loop, and a while loop

a for loop takes each item in an iterable (somethnig we can iterate over, like
 list or a tuple or a range) and repeats the action over it all
 
 for each_thing in my_iterable:
    do_this_action()

the each_thing can be like int or num, or a defined variable
"""

# %% 
# Necessary parts of an iterable for loop and a basic example
number_list = [1, 2, 3, 4, 5] # created a number list to use as iterable

for each_number in number_list: # so for every item in the whole list
    print(each_number*2) # needs an action 
    
# %%
# instead of number list, you could use range (last number is exclusive)

for i in range (6):     # i is often used here in place of item
    print(i*2)
    
# %%
# Can also use for loops for functions
days_list = [
"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]

for day in days_list:
    print(day, "has a length of", len(day))
    
# %%
# We can build on that and create a shared list for days_and_length
# This bit feels important for my "closest to zero" exercise

days_list = [
"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]
days_and_length = [] # creating a blank list

# Use the for look to append  day and number of letters each time to the list
for day in days_list:
    days_and_length.extend([day, len(day)])
    
days_and_length

# %%
grams = [100000, 7899900, 967312, 49185, 6100]

for weight in grams:
    kg = (weight/1000)
    print(kg)
    
# %%
""" While loops
For loops will iteratue over a specified number of things, but a while loop 
will go until it meets a certain condition
e.g., 
condition - value
while condition is True:
do_this_thing()

Looking at the charts, it seems like it'll go until it hits the false condition
just once

Set out like for loop, just with word while then a conditional statement, and
finished with a colon. Then, if condition is met, say what you want the code to
do. 

Important to note that condition will change at some point, so the while loop
will stop then, or it'll continue running "forever" (or unless we stop it)
"""

# %%
stop_value = 0
while stop_value < 5:
    print (stop_value)
    stop_value += 1
 # this adds something to a value, without this line it keeps going and 
 # returning zero
    

# %%
temperature = 40
while temperature > 20:
    print("it's way too hot, it's", temperature, "degrees")
    temperature -= 2
    
# Exercise 5.1
# %%
    """
If, elif, and else 

Not loops, but fall under "control flow". 

These are conditional, and if the appropriate argument is met, the action is
completed. if it's not, python will move to an elif (if there is one), and if
that condition is met the action associated with the elif will be executed.

finally, if none of these conditions are met, the actions in the else block will
be carried out

e.g.,
if condition_1:
    do_action_1()
elif condition_2:
    do_action_2()
else:
    do_action_3()
    

These if, elif, else statements need a condition, so we need a double == sign
for checking equivalency

It's ok to just have an if, or just an if and an else

If and Else are at same indentation level, with respective commands indented

Can use multiple conditions too
    """
 
 # %% 
 # Example
my_height = 17
if (my_height == 5):
    print("We're the same height")

elif (my_height > 7) & (my_height < 10):
    print("You're tall")

else:
    print("Your height is different.")
    
# %%
""" List comprehension

This is something I know I struggle with, creating a blank list and extended it
with a loop
"""

# %%
numbers = [1,2,3,4,5,6,7,8,9,10]
double_list = [] #blank list to put the output in

for each_number in numbers:
    double_list.append(each_number * 2)

print(double_list)

# %%
"""
Another way of looking at it is by using list comprehension, which compresses 
the code into a single line.

 Here, we'd make a list and say "for each number in the list, double it. Use 
 square brackets to make a new list.
"""

# %% 
# Other way of doing it
numbers = [1,2,3,4,5,6,7,8,9,10]

double_list_comprehension = [(each_number * 2) for each_number in numbers]

double_list_comprehension


# %%
""" Functions

3 types of functions:
1. Built in functions - the kind built into python
2. User defined functions, created by users for specific things e.g., using the 
def keyword 
3. Anonymous functions, lambda functions

This training focuses on user defined functions
Functions help us write chunks of reusable code. This will create blocks of 
code that are focused on one job or procedure, as well as making sure code is 
easier to read and reproduce.

Functions are structured like this:
def my_function_name(parameter_1, parameter_2):
    function_actions
    ...
    return function_output
    

So it starts with def (define), followed by function name, then brachets with 
parameters in. Finished wuth a colon like loops and control flow and then return
at the end to return whatever value is needed. Nothing written after return 
will be executed. without return written, nothing will be given as an output

def add_two_values(value 1, value 2):
    total = value_1 + value_2
    return total
    
so then you can just do:
add_two_values (1,2)

"""

# %%
# Exercise 6.2: write function to convert farneheit to celsius

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return round(celsius, 1)

fahrenheit_to_celsius(fahrenheit = 21)

 # %%

# Named parameters:
# Important to use descriptive parameter names and pass arguments using 
# an = sign

def add_two_values(value_1=3, value_2=10)

# %%
# We can also set default values when declaring a function

def add_two_values(value_1=3,value_2=10):
    total = value_1 + value_2
    return total

add_two_values()

# %%
add_two_values(value_2=15) # default for value_1 stays at 3

# %%
def add_two_values (value_1=3,value_2=10):
"""_
summary_
     This function will add together two values
    
    value_1 : The first value to add
    value_2 : The second value to add
    
    Returns: The sum / concatenation of the two values specificed.
    
    Examples:
    
    add_two_values(1, 2) 
    returns 3
    
    add_two_values(4.7,  3.2) 
    returns 7.9 
    
    add_two_values("Hello", "World") 
    returns "HelloWorld" (The + symbol concatenates strings)
    
    Errors will occur if adding together strings and numerics, unless you
    use str() around the numeric.
    """

 total = value_1 + value_2
    return total

# %%
help(add_two_values)
# %%
