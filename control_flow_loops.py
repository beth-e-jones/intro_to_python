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
