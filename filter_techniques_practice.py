import pandas as pd

supermarket_sales = pd.DataFrame({
  'Product': ['Cereal', 'Milk', 'Eggs', 'Cereal', 'Milk', 'Eggs'],
  'Supermarket': ['Super A', 'Super A', 'Super A', 'Super B', 'Super B', 'Super B'],
  'Sales': [25, 35, 45, 60, 75, 90]
})

grouped_df = supermarket_sales.groupby('Product')
filtered_df = grouped_df.filter(lambda x: x['Sales'].sum() > 100)
print(filtered_df)

# Good job so far, Stellar Navigator!

# Let's elevate this a notch. In the starter code, the DataFrame is filtered to display products with a total sales value greater than 250. Could you alter the code to include products with mean sales more than or equal to 215 instead? You will need to modify the lambda function accordingly. Let's begin coding!

sales = pd.DataFrame({
  'Product': ['Milk', 'Eggs', 'Bread', 'Milk', 'Eggs', 'Bread'],
  'Region': ['North', 'North', 'North', 'South', 'South', 'South'],
  'Sales': [120, 200, 210, 150, 230, 220]
})

grouped_sales = sales.groupby('Product')
filtered_sales = grouped_sales.filter(lambda x: x['Sales'].mean() >= 215)
print(filtered_sales)

# Alright, space traveler, let's enhance your data analysis skills. Consider the following code.

# Your task is to complete the code so that it correctly filters out only the products of which the total quantity sold across all stores exceeds 100.

# Grocery store sales dataset
sales = pd.DataFrame({
    'Product': ['Apple', 'Banana', 'Pear', 'Apple', 'Banana', 'Pear', 'Apple'],
    'Store': ['Store1', 'Store2', 'Store3', 'Store1', 'Store2', 'Store3', 'Store2'],
    'Quantity': [30, 20, 50, 60, 40, 20, 75]
})

# Group the data by Product
grouped = sales.groupby('Product')

# TODO: Add a line of code to filter 
# Products with a total quantity of above 100 across all stores.
filtered = grouped.filter(lambda x: x['Quantity'].sum() > 100)
print(filtered)

# TODO: Create a DataFrame 'inventory', which consists of product names, store names and quantities of the respective products sold at each store.
inventory = pd.DataFrame({
    'Product': ['Shirts', 'Jeans', 'Pants', 'Coats', 'Scarves', 'Shoes', 'Gloves', 'Glasses'],
    'Stores': ['Store_1', 'Store_3', 'Store_2', 'Store_3', 'Store_1', 'Store_1', 'Store_3', 'Store_2'],
    'Quantity': [200, 890, 25, 12, 100, 5, 50,29]
})

# TODO: Use 'groupby' function to group the DataFrame by 'Product'
grouped = inventory.groupby('Product')

# TODO: Use 'filter' function to filter out the groups that have a mean sold quantity greater than 30
filter = grouped.filter(lambda x: x['Quantity'].mean() > 30)

# TODO: Print the resulting DataFrame.
print(filter)