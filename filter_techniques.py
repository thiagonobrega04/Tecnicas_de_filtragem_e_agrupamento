import pandas as pd

# Introduction
# Today, we're approaching data analysis from a new angle by applying filtering to grouped DataFrames. We will review DataFrame grouping and introduce filtering, illustrating these concepts with examples. By the end of this lesson, you will be equipped with the necessary skills to effectively group and filter data.

# Recap of Grouping in Pandas
# As a quick recap, pandas is a highly influential Python module for data analysis, with powerful classes such as DataFrames at its core. DataFrames are data tables, and you can group the data within them using the groupby() function. Here is an example of grouping data within a DataFrame by 'Product':

sales = pd.DataFrame({
  'Product': ['Apple', 'Banana', 'Pear', 'Apple', 'Banana', 'Pear'],
  'Store': ['Store1', 'Store1', 'Store1', 'Store2', 'Store2', 'Store2'],
  'Quantity': [20, 30, 40, 50, 60, 70]
})

grouped = sales.groupby('Product')
print(grouped.get_group('Apple'))  # printing one group for an example
'''Output:
  Product   Store  Quantity
0   Apple  Store1        20
3   Apple  Store2        50
'''

# Recap of Lambda Functions
# To filter grouped data, we will need functions. Let's recall how to easily create and use them.

# In Python, lambda functions are small anonymous functions. They can take any number of arguments but only have one expression.

# Consider a situation where we use a function to calculate the total price after adding the sales tax. In a place where the sales tax is 10%, the function to calculate the total cost could look like:

# Regular Function

def add_sales_tax(amount):
    return amount + (amount * 0.10)

print(add_sales_tax(100))  # 110 

# Replacing the function with a compact lambda function is handy when it is simple and not used repeatedly. The syntax for lambda is lambda var: expression, where var is the function's input variable and expression is what this function returns.

# The above add_sales_tax function can be replaced with a lambda function as follows:

# Lambda Function

add_sales_tax = lambda amount : amount + (amount * 0.10)
print(add_sales_tax(100))  #110

# Lambda functions are handy when used inside other functions or as arguments in functions like filter(), map() etc.

# Example of a Boolean Lambda Function
# A Boolean Lambda function always returns either True or False. Let's imagine a case where we want to know whether a number is even or odd. We can easily accomplish this using a Boolean Lambda function.

# Here's how we can define such a function:

is_even = lambda num: num % 2 == 0
print(is_even(10))  # True

# The preceding two lines of code create a Boolean Lambda function named is_even. This function takes a number (named num) as an argument, divides it by 2, and then checks if the remainder is 0. It returns the condition's value, either True or False.

# Boolean lambda functions are fantastic tools for quickly evaluating a condition. Their applications are broad, especially when you're manipulating data with pandas. They can be used in various ways, including sorting, filtering, and mapping.

# Filtering a Grouped DataFrame
# Boolean selection does not apply to grouped dataframes. Instead, we use the filter() function, which takes a boolean function as an argument. For instance, let's keep products with a summary quantity greater than 90.

grouped = sales.groupby('Product')
filtered_df = grouped.filter(lambda x: x['Quantity'].sum() > 90)
print(filtered_df)
'''Output:
  Product   Store  Quantity
2    Pear  Store1        40
5    Pear  Store2        70
'''

# This command yields the rows from the grouped data where the sum of Quantity exceeds 90. Pears are included, as their summary quantity is 40 + 70 = 110.