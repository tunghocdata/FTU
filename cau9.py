import pandas as pd
from datetime import datetime 
from collections import Counter

df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])

# Sort by user_id and timestamp to ensure the stall visits are in order
df = df.sort_values(by=['Person ID', 'Timestamp'])

#user_paths = df.groupby('Person ID')['Shelf ID'].apply(lambda x: ' -> '.join(map(str, x))).reset_index()


# Remove consecutive duplicate shelves for each user
df['previous_shelf'] = df.groupby('Person ID')['Shelf ID'].shift(1)
df_filtered = df[df['Shelf ID'] != df['previous_shelf']]

# Create a list of shelves visited for each user
#shelves_visited = df_filtered.groupby('Person ID')['Shelf ID'].apply(list).reset_index()

filtered_stalls = df[(df['Picking up item'] == True) & (df['Putting item into bag'] == True)]

# Group by the stall (assuming the column for stall names is 'stall_name') and count how many products were purchased
top_stalls = filtered_stalls.groupby('Shelf ID').size().reset_index(name='purchase_count')

# Sort by purchase count in descending order
top_stalls = top_stalls.sort_values(by='purchase_count', ascending=False)

# Select the top 3 stalls with the most purchased products
top_3_stalls = top_stalls.head(3)

# Display the result
print(top_3_stalls)
