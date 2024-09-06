import pandas as pd
from datetime import datetime 
from collections import Counter

df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])


df1 = pd.read_csv('03_Customer_Behavior_Data.csv')

df2 = pd.read_csv('03_Item_Information_Data.csv')

merge_df = pd.merge(df1,df2, on=['Item ID','Shelf ID'])
merge_df = merge_df[merge_df['Marketing strategy'] == True] 

filtered_data = merge_df[(merge_df['Picking up item'] == True) & (merge_df['Putting item into bag'] == True)]

item_counts = filtered_data.groupby(['Marketing strategy', 'Item ID', 'Shelf ID']).size().reset_index(name='Count')

item_counts = item_counts.sort_values(by='Count',ascending = False)
print(item_counts.head(5))
