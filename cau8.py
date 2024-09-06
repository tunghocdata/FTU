import pandas as pd
from datetime import datetime 
from collections import Counter

df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])

filtered_stalls = df[(df['Picking up item'] == True) & (df['Putting item into bag'] == True)]

df["Total"] = df["Looking at item (s)"]+ df["Holding the item (s)"]
# Group by the stall (assuming the column for stall names is 'stall_name') and count how many products were purchased
df = df.groupby('Shelf ID').size().reset_index(name= 'Total')

# Sort by purchase count in descending order
top_stalls = df.sort_values(by="Total", ascending=False)

# Select the top 3 stalls with the most purchased products
top_3_stalls = top_stalls.head(3)

# Display the result
print(top_3_stalls)
