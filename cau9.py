import pandas as pd
from datetime import datetime 
from collections import Counter

df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])

filtered_stalls = df[(df['Picking up item'] == True) & (df['Putting item into bag'] == True)]

# Group by the stall (assuming the column for stall names is 'stall_name') and count how many products were purchased
top_stalls = filtered_stalls.groupby('Shelf ID').size().reset_index(name='purchase_count')

# Sort by purchase count in descending order
top_stalls = top_stalls.sort_values(by='purchase_count', ascending=False)

# Select the top 3 stalls with the most purchased products
top_3_stalls = top_stalls.head(3)

# Display the result
print(top_3_stalls)
