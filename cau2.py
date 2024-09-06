import pandas as pd

df = pd.read_csv('03_Customer_Behavior_Data.csv')


# Filter data where 'Picking up item' and 'Putting item into bag' are TRUE
filtered_data = df[(df['Picking up item'] == True) & (df['Returning item'] == True)]

# Group by 'Age Group' and 'Item ID', and count the occurrences
item_counts = filtered_data.groupby([ 'Item ID', 'Shelf ID']).size().reset_index(name='Count')

# Find the most purchased item per age group
most_purchased = item_counts.loc[item_counts.groupby('Item ID')['Count'].idxmax()]

print(item_counts.head(5))

     Item ID  Shelf ID  Count
17         2         2    134
55         7         0    127
98        12         7    117
108       14         7    116
22         2         7    114
